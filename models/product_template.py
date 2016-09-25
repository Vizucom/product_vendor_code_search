# -*- coding: utf-8 -*-
from openerp.osv import osv, fields


class ProductTemplate(osv.Model):

    _inherit = 'product.template'

    def _get_vendor_codes(self, cr, uid, ids, field_name, args, context):
        if not context:
            context = {}

        res = {}
        for product in self.browse(cr, uid, ids, context):
            res[product.id] = '\n'.join([seller.product_code for seller in product.seller_ids if seller.product_code]) or ''

        return res

    def _get_changed_supplierinfos(obj, cr, uid, ids, context=None):
        ''' If supplierinfo line gets changed, recalculate the related product '''
        res = []
        for supplierinfo in obj.browse(cr, uid, ids):
            res.append(supplierinfo.product_id.id)

        return res

    _columns = {
        'vendor_codes': fields.function(_get_vendor_codes, type='char', string='Vendor Codes', store={
            'product.supplierinfo': (_get_changed_supplierinfos, ["product_id", "product_code"], 10)
        })
    }
