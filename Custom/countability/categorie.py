from odoo import models, fields


class Categorie(models.Model):
    _name = 'categorie'
    _description = 'categorie different'


piece_comptable_id = fields.One2many('piece.comptable', 'categorie_id')
