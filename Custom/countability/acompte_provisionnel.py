from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class AcompteProvisionnel(models.Model):
    _name = 'acompte.prov'
    _description = 'acompte provisionnel'

    @api.constrains('year')
    def check_statut(self):
        for rec in self:
            if rec.statut > 3 or rec.statut <= 0:
                raise ValidationError(_('statut incorrect.'))


statut = fields.Integer(string='statut d acompte')
pay= fields.Integer(string='valeur  ')