from odoo import models, fields


class PieceComptable(models.Model):
    _name = 'piece.comptable'
    _description = 'piece comptable'


etat_document_id = fields.Many2one('Etat', 'etat')
categorie_id = fields.Many2one('categorie', 'Categorie')
