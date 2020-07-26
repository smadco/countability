from odoo import models, fields, api, _


class HospitalPatient(models.Model):
    _inherit = 'sale.order'
    demo_name = fields.Char(string='patient name')


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Record'
    _rec_name = 'demo_name'
    demo_name = fields.Char(string='name', required=True)
    demo_age = fields.Integer(string='age')
    notes = fields.Text(string='notes')
    image = fields.Binary(string='Image')
    name = fields.Char(string='test')
    name_seq = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], default='male', string="gender")

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
            result = super(HospitalPatient, self).create(vals)
            return result
