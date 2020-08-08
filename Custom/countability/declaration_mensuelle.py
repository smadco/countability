from odoo import models, fields


class DeclarationMensuelle(models.Model):
    _name = 'declaration.mensuelle'
    _description = 'declaration mensuelle'

    pay = fields.Integer(string='valeur a payé')
    client_id = fields.Many2one('acc.client', 'client_name')
