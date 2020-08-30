from odoo import models, fields


class Categorie(models.Model):
    _name = 'categorie'
    _description = 'categorie different'
    _rec_name = 'categorie_name'

    categorie_name=fields.Char(string='Nom de la catégorie', required=True)


    piece_comptable_ids = fields.One2many(comodel_name='piece.comptable',inverse_name='categorie_id')

