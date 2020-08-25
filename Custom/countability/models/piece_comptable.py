from odoo import models, fields


class PieceComptable(models.Model):
    _name = 'piece.comptable'
    _description = 'piece comptable'

    piece_name = fields.Char(string='Désignation du document', required=True, track_visibility="always")

    #etat_document_id = fields.Many2one('Etat', 'etat')
    categorie_id = fields.Many2one(comodel_name='categorie')
    declration_mensuelle_id = fields.Many2one(comodel_name='declaration.mensuelle')
    # gestionnaire_id = fields.Many2one(comodel_name='gestionnaire')
    client_piece_comptable_ids = fields.Many2one(comodel_name='Acc.client')
    etat_id = fields.Many2one(comodel_name='piece.comptable')