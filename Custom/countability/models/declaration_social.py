from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class DeclarationSocial(models.Model):
    _name = 'declaration.social'
    _description = 'declaration social'

    @api.constrains('trimestre')
    def check_trimestre(self):
        for rec in self:
            if rec.trimestre > 3 or rec.trimestre <= 0:
                raise ValidationError(_('trimestre incorrect.')) \
 \
    @api.constrains('year')
    def check_year(self):
        for rec in self:
            if rec.year > 12 or rec.year <= 0:
                raise ValidationError(_('année incorrect.'))

    trimestre = fields.Integer(string='trimestre')
    year = fields.Integer(string='année')
    pay = fields.Integer(string='valeur')
    client_id = fields.Many2one('acc.client', 'client_name')
     # etat = fields.Text(string='état de declaration')
