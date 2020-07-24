from odoo import models, fields


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Record'
    demo_name = fields.Char(string='name', required=True)
    demo_age = fields.Integer(string='age')
    notes = fields.Text(string='notes')
    image = fields.Binary(string='Image')
