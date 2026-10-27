from odoo import fields, models


class DentalPatientImage(models.Model):
    _name = 'dental.patient.image'
    _description = 'Dental Patient Image'
    _order = 'date desc, id desc'

    patient_id = fields.Many2one(
        'dental.patient',
        string='Patient',
        required=True,
        ondelete='cascade',
    )
    image = fields.Image(
        string='Image',
        required=True,
        max_width=1920,
        max_height=1920,
    )
    image_thumb = fields.Image(
        string='Thumbnail',
        related='image',
        max_width=300,
        max_height=300,
        store=True,
    )
    category = fields.Selection([
        ('start', 'Start'),
        ('progress', 'Progress'),
        ('retention', 'Retention'),
        ('models', 'Models'),
        ('pan', 'PAN'),
        ('ceph', 'CEPH'),
        ('occl', 'Occl'),
        ('various', 'Various'),
        ('hygiene', 'Hygiene'),
        ('library', 'Library'),
    ], string='Category', required=True, default='start')
    date = fields.Date(string='Date', required=True, default=fields.Date.today)
    name = fields.Char(string='Description')
