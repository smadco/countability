from odoo import models, fields


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Patient Record'
    _rec_name = 'demo_name'
    demo_name = fields.Char(string='name', required=True)
    demo_age = fields.Integer(string='age')
    notes = fields.Text(string='notes')
    image = fields.Binary(string='Image')
    name = fields.Char(string='test')
