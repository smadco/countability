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
    nom_geron = fields.Char(string='nom du gerant')
    num_geron = fields.Integer(string='numero gerant')
    num_fixe = fields.Integer(string='numero fixe')
    num_portable = fields.Integer(string='numero portable')
    notes = fields.Text(string='notes')
    image = fields.Binary(string='Image')
    activite = fields.Text(string='activite')
    num_AEP = fields.Integer(string='numero AEP')
    capitale = fields.Integer(string="capitale en Dinar")
    siege_social = fields.Text(string='siege social')

    gestionnaire_id = fields.Many2one(comodel_name='gestionnaire')
    dossier_juridique_ids = fields.One2many(comodel_name='dossier.juridique', inverse_name='clients_jur_ids')
    piece_comptable_id = fields.One2many(comodel_name='piece.comptable', inverse_name='client_piece_comptable_ids')
    client_declaration_mensuelle_ids = fields.One2many(comodel_name='declaration.mensuelle', inverse_name='declaration_mensuelle_id')
    client_acompte_previsionnel_ids = fields.One2many(comodel_name='acompte.prov', inverse_name='acompte_previsionnel_id')
    client_bilan_annuel_ids = fields.One2many(comodel_name='billan.annuel', inverse_name='bilan_annuel_id')
    client_declaration_social_ids = fields.One2many(comodel_name='declaration.social', inverse_name='declaration_social_id')
