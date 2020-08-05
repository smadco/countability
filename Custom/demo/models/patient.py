from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _inherit = 'sale.order'
    demo_name = fields.Char(string='patient name')


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Record'
    _rec_name = 'demo_name'

    @api.constrains('demo_age')
    def check_age(self):
        for rec in self:
            if rec.demo_age <= 5:
                raise ValidationError(_('The age must be greater than 5'))

    @api.depends('demo_age')
    def set_age_group(self):
        for rec in self:
            if rec.demo_age:
                if rec.demo_age < 18:
                    rec.age_group = 'minor'
                else:
                    rec.age_group = 'major'

    demo_name = fields.Char(string='name', required=True, track_visibility="always")
    demo_age = fields.Integer(string='age', track_visibility="always")
    notes = fields.Text(string='notes')
    image = fields.Binary(string='Image')
    name = fields.Char(string='test')
    name_seq = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], default='male', string="gender")
    age_group = fields.Selection([
        ('major', 'Major'),
        ('minor', 'Minor'),
    ], string='Age Group', compute='set_age_group')

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
            result = super(HospitalPatient, self).create(vals)
            return result
