from odoo import models, fields


class DentalVisit(models.Model):
    _name = "dental.visit"
    _description = "Dental Visit"
    _rec_name = "visit_date"
    _order = "visit_date desc, id desc"

    patient_id = fields.Many2one(
        'dental.patient',
        string="Patient",
        required=True,
        ondelete='cascade',
    )
    visit_date = fields.Date(string="Visit Date", required=True, default=fields.Date.today)
    treating_doctor_id = fields.Many2one('dental.doctor', string='Treating Doctor')
    notes = fields.Text(string="Notes")
    line_ids = fields.One2many('dental.visit.line', 'visit_id', string='Treatment Lines')


class DentalVisitLine(models.Model):
    _name = 'dental.visit.line'
    _description = 'Dental Visit Treatment Line'
    _order = 'id'

    visit_id = fields.Many2one(
        'dental.visit',
        string='Visit',
        required=True,
        ondelete='cascade',
    )
    stage_diagnosis = fields.Char(string='Stage / Diagnosis')
    procedure = fields.Char(string='Procedure')
    notes = fields.Text(string='Notes')