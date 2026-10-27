from odoo import models ,fields

class DentalDoctor(models.Model):
    _name ="dental.doctor"
    _description = "Dental Doctor"
    _rec_name = "name"
    _order = "name"
    
    name = fields.Char(string="Doctor", required=True)
    
    