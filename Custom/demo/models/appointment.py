# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "appointment_data desc "

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('new'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
        result = super(HospitalAppointment, self).create(vals)
        return result

    name = fields.Char(string='Appointment ID', required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))


def _get_default_note(self):
    return "nothing special"


def _get_default_name(self):
    return "1"


patient_id = fields.Many2one('hospital.patient', string='Patient', required=True, default=_get_default_name)
patient_age = fields.Integer('Age', related='patient_id.patient_age')
notes = fields.Text(string='Registration Notes', default=_get_default_note)
appointment_data = fields.Date(string='Data', required=True)
