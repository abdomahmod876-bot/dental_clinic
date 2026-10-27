from odoo import models ,fields

class DentalPatientRace(models.Model):
    _name ="dental.patient.race"
    _description = "Dental Patient Race"
    _rec_name = "name"
    _order = "name"
    name = fields.Char(string="Race", required=True)
   