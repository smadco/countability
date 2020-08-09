from odoo import models, fields


class Gestionnaire(models.Model):
    _name = 'gestionnaire'
    _description = 'gestionnaire'


    gestionnaire_name = fields.Char(string='nom et prenom', required=True, track_visibility="always")
    etat_id = fields.Many2one('etat', 'gestionnaire_name')
