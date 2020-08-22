from odoo import models, fields


class Gestionnaire(models.Model):
    _name = 'gestionnaire'
    _description = 'gestionnaire'
    _rec_name = 'gestionnaire_name' \
                ''

    gestionnaire_name = fields.Char(string='nom et prenom', required=True, track_visibility="always")
    client_ids = fields.One2many(comodel_name='acc.client', inverse_name='gestionnaire_id')
