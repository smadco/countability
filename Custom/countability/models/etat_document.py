from odoo import models, fields


# pour utilise mail.thread et mail.activity
# class Etat(models.Model):
#     _inherit = 'sale.order'
#     demo_name = fields.Char(string=' name')

class Etat(models.Model):
    _name = 'etat.doc'
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'etat document'


    #gestionnaire_id = fields.One2many('gestionnaire', 'etat_document_id')
    #piece_comptable_id = fields.One2many('piece.comptable', 'etat_document_id')
    piece_comptable_etat_ids = fields.One2many(comodel_name='piece.comptable',
                                                    inverse_name='etat_id')
    name = fields.Char('name')
