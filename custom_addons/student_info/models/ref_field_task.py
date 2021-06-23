from odoo import models, fields
from odoo import api


class SoRefranceRespatner(models.Model):
    _inherit = "res.partner"

    so_referance_res = fields.Char()


class SoRefranceSale(models.Model):
    _inherit = 'sale.order'

    so_referance_sale = fields.Char()

    @api.onchange('partner_id')
    def chanhe_so_val(self):
        for rec in self:

            if self.partner_id.company_type == 'person' and not self.partner_id.so_referance_res:
                print('\n\n\n', 'yes tame addkaro')
                rec.write(
                    {'so_referance_sale': self.partner_id.parent_id.so_referance_res})
            else:
                rec.write(
                    {'so_referance_sale': self.partner_id.so_referance_res})

    def _prepare_invoice(self):
        vals = super(SoRefranceSale, self)._prepare_invoice()
        print(f"\n\n\n\nthis is prepare{vals}")
        vals.update({'so_referance_acc': self.so_referance_sale})
        return vals


class SoRefranceAccount(models.Model):
    _inherit = "account.move"

    so_referance_acc = fields.Char()

    @api.onchange('partner_id')
    def chanhe_so_val(self):
        for rec in self:

            if self.partner_id.company_type == 'person' and not self.partner_id.so_referance_res:
                print('\n\n\n', 'yes tame addkaro')
                rec.write(
                    {'so_referance_acc': self.partner_id.parent_id.so_referance_res})
            else:
                rec.write(
                    {'so_referance_acc': self.partner_id.so_referance_res})
