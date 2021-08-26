#This file is part stock_catalogue module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields, sequence_ordered


class Catalogue(ModelSQL, ModelView):
    'Catalogue of products for a warehouse'
    __name__ = 'stock.location.catalogue'
    name = fields.Char('Name', required=True)
    code = fields.Function(fields.Integer('Code', readonly=True), 'get_code')
    location = fields.Many2One('stock.location', 'Location', required=True,
        help='Location which will be used for the \'From location\' field')
    lines = fields.One2Many('stock.location.catalogue.line', 'catalogue', 'Lines')

    def get_code(self, name=None):
        return self.id


class CatalogueLine(sequence_ordered(), ModelSQL, ModelView):
    'Lines of products for a catalogue'
    __name__ = 'stock.location.catalogue.line'

    catalogue = fields.Many2One('stock.location.catalogue', 'Catalogue',
        required=True, readonly=True, ondelete='CASCADE')
    product = fields.Many2One('product.product', 'Product', required=True)
    max_quantity = fields.Float('Maximum quantity', required=True,
        digits='unit')
    notes = fields.Char('Notes')
    unit = fields.Function(fields.Many2One('product.uom', "Unit",),
        'on_change_with_unit')

    @fields.depends('product')
    def on_change_with_unit(self, name=None):
        if self.product:
            return self.product.default_uom.id
