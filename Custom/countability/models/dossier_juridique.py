from odoo import models, fields


class DossierJuridique(models.Model):
    _name = 'dossier.juridique'
    _description = 'dossier juridique'

    patent = fields.Char(string='patent')
    RC = fields.Char(string='R.C')
    statu = fields.Char(string='statu')
    cer_cnss = fields.Binary(string='certificat d"attitude CNSS')
    cer_travail = fields.Binary(string='certificat de travail')
