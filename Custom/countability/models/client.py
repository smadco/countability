from odoo import models, fields


class AccClient(models.Model):
    _name = 'acc.client'
    _description = 'client record'
    _rec_name = 'client_name'

    client_name = fields.Char(string='nom et prenom or raison social', required=True, track_visibility="always")
    num_matricule_fiscal = fields.Integer(string='numero matricul fiscal', required=True)
    identification_unique = fields.Char(string='identification unique')
    cnss_regional = fields.Char(string='cnss regional')
    cnss_independent = fields.Char(string='cnss independent')
    email = fields.Char(string='email')
    nom_geron = fields.Char(string='nom du geron')
    num_geron = fields.Integer(string='numero geron')
    num_fixe = fields.Integer(string='numero fixe')
    num_portable = fields.Integer(string='numero portable')
    notes = fields.Text(string='notes')
    image = fields.Binary(string='Image')
    activite = fields.Text(string='activite')
    num_AEP = fields.Integer(string='numero AEP')
    capitale = fields.Integer(string="capitale en Dinar")
    siege_social = fields.Text(string='siege social')