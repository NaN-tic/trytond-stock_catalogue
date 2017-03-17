#This file is part country_zip module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields

__all__ = ['Catalogue', 'CatalogueLines']


class Catalogue(ModelSQL, ModelView):
    'Catalogue of products for a warehouse'
    __name__ = 'stock.location.catalogue'

    lines = fields.One2Many('stock.location.catalogue.line', 'catalogue', 'Lines')
    name = fields.Char('Name', required=True)
    code = fields.Function(fields.Integer('Code', readonly=True),
            'get_code_value')
    users = fields.One2Many('res.user', 'catalogue', 'Users')
    location = fields.Many2One('stock.location', 'Location', required=True,
        help='Location which will be used for the \'From location\' field')

    def get_code_value(self, name=None):
        return self.id


class CatalogueLines(ModelSQL, ModelView):
    'Lines of products for a catalogue'
    __name__ = 'stock.location.catalogue.line'

    catalogue = fields.Many2One('stock.location.catalogue', 'Catalogue',
        required=True, readonly=True, ondelete='CASCADE')
    product = fields.Many2One('product.product', 'Product', required=True)
    max_quantity = fields.Integer('Maximum quantity', required=True)
    notes = fields.Char('Notes')
