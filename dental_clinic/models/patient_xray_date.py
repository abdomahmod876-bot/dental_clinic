from odoo import models ,fields


class DentalPatientXrayDate(models.Model):
    _name = "dental.patient.xray.date"
    _description = "Dental Patient Xray Date"
    _rec_name = "xray_date"
    _order = "xray_date desc, id desc"

    xray_date = fields.Date(string="X-ray Date", required=True)
    patient_id = fields.Many2one(
        'dental.patient',
        string="Patient",
        ondelete='cascade',
    )
    