from odoo import models, fields


class BilanAnnuel(models.Model):
    _name = 'billan.annuel'
    _description = 'billan annuel'

    total_pay = fields.Integer(string='payment total')