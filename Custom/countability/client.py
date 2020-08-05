from odoo import models, fields


class AccClient(models.Model):
    _name = 'acc.client'
    _description = 'client record'

    client_name = fields.Char(string='nom et prenom or raison social', required=True, track_visibility="always")
    num_matricule_fiscal = fields.Integer(string='numero matricul fiscal', required=True)
    identification_unique = fields.Char(string='identification unique')
    cnss_regional = fields.Char(string='cnss regional')
    cnss_independent = fields.Char(string='cnss independent')
    email = fields.Char('email')
    nom_geron = fields.Char(string='nom du geron')
    num_geron = fields.Integer(string='numero geron')
    num_fixe = fields.Integer(string='numero fixe')
    num_portable = fields.Integer(string='numero portable')
    activite = fields.Text(string='activite')
    num_AEP = fields.Integer(string='numero AEP')
    capitale = fields.Integer(string="capitale en Dinar")

