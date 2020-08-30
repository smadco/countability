from odoo import models, fields ,api ,_
from odoo.exceptions import ValidationError

class BilanAnnuel(models.Model):
    _name = 'billan.annuel'
    _description = 'billan annuel'

    @api.constrains('year')
    def check_year(self):
        for rec in self:
            if rec.year >= 2030 or rec.year <= 2019:
                raise ValidationError(_('année incorrect.'))

    total_pay = fields.Integer(string='payment total')
    bilan_annuel_id = fields.Many2one(comodel_name='Acc.client')
    year = fields.Integer(string='année')
    status = fields.Text(string='status')