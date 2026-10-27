from odoo import models ,fields

class DentalPatientCity(models.Model):
    _name ="dental.patient.city"
    _description = "Dental Patient City"
    _rec_name = "name"
    _order = "name"
    
    name = fields.Char(string="City", required=True)