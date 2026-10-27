from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class DentalPatient(models.Model):
    _inherit = ['mail.thread']
    _name = 'dental.patient'
    _description = 'Dental Patient'
    _rec_name = 'name'
    _order = 'patient_id, id'

    patient_id = fields.Integer(string='Patient ID', copy=False)
    first_name = fields.Char(string='First Name', required=True)
    middle_name = fields.Char(string='Middle Name')
    middle_initial = fields.Char(string='MI')
    last_name = fields.Char(string='Last Name')
    name = fields.Char(string='Name', compute='_compute_name', store=True)
    age = fields.Integer(string='Age', compute='_compute_age')
    sex = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Sex')
    birthdate = fields.Date(string='Birthdate')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    city_id = fields.Many2one('dental.patient.city', string='City')
    address = fields.Char(string='Address')
    race_id = fields.Many2one('dental.patient.race', string='Race')
    class_id = fields.Selection([
        ('I', 'I'),
        ('II', 'II'),
        ('III', 'III'),
    ], string='Class')
    class_notes = fields.Char(string='Class Notes')
    referring_doctor_id = fields.Many2one('dental.doctor', string='Referring Doctor')
    treating_doctor_id = fields.Many2one('dental.doctor', string='Treating Doctor')
    current_stage = fields.Selection([
        ('installation', 'Installation'),
        ('follow_up', 'Follow-up'),
        ('removal', 'Removal'),
    ], string='Current Stage')
    comments = fields.Text(string='Comments')
    photo = fields.Image(string='Photo', max_width=1024, max_height=1024)
    xray_date_ids = fields.One2many('dental.patient.xray.date', 'patient_id', string='X-ray Dates')
    visit_ids = fields.One2many('dental.visit', 'patient_id', string='Visits')
    image_ids = fields.One2many('dental.patient.image', 'patient_id', string='Images')
    image_start_ids = fields.One2many(
        'dental.patient.image', 'patient_id', string='Start Images',
        domain=[('category', '=', 'start')], context={'default_category': 'start'},
    )
    image_progress_ids = fields.One2many(
        'dental.patient.image', 'patient_id', string='Progress Images',
        domain=[('category', '=', 'progress')], context={'default_category': 'progress'},
    )
    image_retention_ids = fields.One2many(
        'dental.patient.image', 'patient_id', string='Retention Images',
        domain=[('category', '=', 'retention')], context={'default_category': 'retention'},
    )
    image_models_ids = fields.One2many(
        'dental.patient.image', 'patient_id', string='Models',
        domain=[('category', '=', 'models')], context={'default_category': 'models'},
    )
    image_pan_ids = fields.One2many(
        'dental.patient.image', 'patient_id', string='PAN Images',
        domain=[('category', '=', 'pan')], context={'default_category': 'pan'},
    )
    image_ceph_ids = fields.One2many(
        'dental.patient.image', 'patient_id', string='CEPH Images',
        domain=[('category', '=', 'ceph')], context={'default_category': 'ceph'},
    )
    image_occl_ids = fields.One2many(
        'dental.patient.image', 'patient_id', string='Occl Images',
        domain=[('category', '=', 'occl')], context={'default_category': 'occl'},
    )
    image_various_ids = fields.One2many(
        'dental.patient.image', 'patient_id', string='Various Images',
        domain=[('category', '=', 'various')], context={'default_category': 'various'},
    )
    image_hygiene_ids = fields.One2many(
        'dental.patient.image', 'patient_id', string='Hygiene Images',
        domain=[('category', '=', 'hygiene')], context={'default_category': 'hygiene'},
    )
    image_library_ids = fields.One2many(
        'dental.patient.image', 'patient_id', string='Library Images',
        domain=[('category', '=', 'library')], context={'default_category': 'library'},
    )
    image_count_all = fields.Integer(compute='_compute_image_counts')
    image_count_start = fields.Integer(compute='_compute_image_counts')
    image_count_progress = fields.Integer(compute='_compute_image_counts')
    image_count_retention = fields.Integer(compute='_compute_image_counts')
    image_count_models = fields.Integer(compute='_compute_image_counts')
    image_count_pan = fields.Integer(compute='_compute_image_counts')
    image_count_ceph = fields.Integer(compute='_compute_image_counts')
    image_count_occl = fields.Integer(compute='_compute_image_counts')
    image_count_various = fields.Integer(compute='_compute_image_counts')
    image_count_hygiene = fields.Integer(compute='_compute_image_counts')
    image_count_library = fields.Integer(compute='_compute_image_counts')

    _patient_id_unique = models.Constraint(
        'unique(patient_id)',
        'Patient number is already used!'
    )
    _patient_id_positive = models.Constraint(
        'check(patient_id > 0)',
        'Patient number must be greater than 0!'
    )

    @api.constrains('patient_id')
    def _check_patient_id(self):
        for patient in self:
            if patient.patient_id is not None and patient.patient_id <= 0:
                raise ValidationError('Patient number must be greater than 0!')

    @api.depends('first_name', 'middle_name', 'middle_initial', 'last_name')
    def _compute_name(self):
        for patient in self:
            parts = [
                patient.first_name or '',
                patient.middle_name or patient.middle_initial or '',
                patient.last_name or '',
            ]
            patient.name = ' '.join(part.strip() for part in parts if part and part.strip())

    @api.depends('birthdate')
    def _compute_age(self):
        today = fields.Date.today()
        for patient in self:
            if not patient.birthdate:
                patient.age = 0
                continue
            patient.age = (
                today.year
                - patient.birthdate.year
                - ((today.month, today.day) < (patient.birthdate.month, patient.birthdate.day))
            )

    @api.depends('image_ids', 'image_ids.category')
    def _compute_image_counts(self):
        categories = (
            'start', 'progress', 'retention', 'models', 'pan',
            'ceph', 'occl', 'various', 'hygiene', 'library',
        )
        for patient in self:
            images = patient.image_ids
            patient.image_count_all = len(images)
            for category in categories:
                field_name = f'image_count_{category}'
                setattr(patient, field_name, len(images.filtered(lambda image: image.category == category)))

    @api.model
    def _get_patient_sequence(self):
        sequence = self.env['ir.sequence'].search([
            ('code', '=', 'dental.patient'),
            ('company_id', '=', self.env.company.id),
        ], limit=1)
        if not sequence:
            sequence = self.env['ir.sequence'].search([
                ('code', '=', 'dental.patient'),
                ('company_id', '=', False),
            ], limit=1)
        if not sequence:
            raise UserError('The dental patient sequence is not configured.')
        return sequence

    @api.model
    def _next_patient_id(self):
        sequence = self._get_patient_sequence()
        max_patient = self.search([('patient_id', '>', 0)], order='patient_id desc', limit=1)
        max_id = max_patient.patient_id or 0
        candidate = max(int(sequence.number_next or 1), int(max_id) + 1)
        while self.search_count([('patient_id', '=', candidate)]):
            candidate += 1
        sequence.number_next = candidate + 1
        return candidate

    @api.model_create_multi
    def create(self, vals_list):
        prepared_vals_list = []
        for vals in vals_list:
            vals = dict(vals)
            patient_id = vals.get('patient_id')
            if patient_id in (None, False, ''):
                vals['patient_id'] = self._next_patient_id()
            else:
                manual_id = int(patient_id)
                if manual_id <= 0:
                    raise ValidationError('Patient number must be greater than 0!')
                sequence = self._get_patient_sequence()
                if int(sequence.number_next or 1) <= manual_id:
                    sequence.number_next = manual_id + 1
            prepared_vals_list.append(vals)
        return super().create(prepared_vals_list)
