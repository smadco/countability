from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class DeclarationMensuelle(models.Model):
    _name = 'declaration.mensuelle'
    _description = 'declaration mensuelle'
    # _rec_name = 'combination'

    @api.constrains('month')
    def check_month(self):
        for rec in self:
            if rec.month >= 13 or rec.month <= 0:
                raise ValidationError(_('mois incorrect.'))

    @api.constrains('year')
    def check_year(self):
        for rec in self:
            if rec.year >= 2050 or rec.year <= 2019:
                raise ValidationError(_('année incorrect.'))

    pay = fields.Integer(string='valeur a payé')
    client_id = fields.Many2one('acc.client', 'client_name')
    month = fields.Integer(string='mois')
    year = fields.Integer(string='année')
    piece_comptable_ids = fields.One2many(comodel_name='piece.comptable',inverse_name='declration_mensuelle_id')
    client_ids = fields.One2many(comodel_name='acc.client',inverse_name='gestionnaire_id')
    # @api.depends('month', 'year')
    # def _compute_fields_combination(self):
    #     for test in self:
    #         test.combination = test.month + ' ' + test.year
    declaration_mensuelle_id = fields.Many2one(comodel_name='Acc.client')
    # combination = fields.Char(string='Combination', compute='_compute_fields_combination')

