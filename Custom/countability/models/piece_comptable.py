from odoo import models, fields


class PieceComptable(models.Model):
    _name = 'piece.comptable'
    _description = 'piece comptable'



    categorie_id = fields.Many2one('categorie', 'Categorie')
    piece_comptable_id = fields.One2many(comodel_name='declaration.mensuelle', inverse_name='declaration_mensuelle_id')
