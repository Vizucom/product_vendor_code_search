# -*- coding: utf-8 -*-
from openerp import models, fields, api


class ProductTemplate(models.Model):

    _inherit = 'product.template'

    @api.depends('seller_ids')
    def _get_vendor_codes(self):

        for record in self:
            record.vendor_codes = '\n'.join([seller.product_code for seller \
                                             in record.seller_ids if seller.product_code]) or ''

    vendor_codes = fields.Char(compute='_get_vendor_codes',
                               string='Vendor Codes',
                               store=True)
