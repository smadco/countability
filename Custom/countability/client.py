from odoo import models, fields


class AccClient(models.Model):
    _name = 'acc.client'
    _description = 'client record'

    client_name = fields.Char(string='nom et prenom or raison social', required=True, track_visibility="always")
    num_matricul_fiscal = fields.Integer(string='numero matricul fiscal', required=True)
