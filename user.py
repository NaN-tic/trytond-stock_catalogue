# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval, Bool

__all__ = ['User', 'UserCatalogue']


class User(metaclass=PoolMeta):
    __name__ = 'res.user'
    catalogue_from_location = fields.Many2One('stock.location', 'From Location',
        domain=[
            ('type', 'in', ['view', 'storage']),
        ], states={
            'required': Bool(Eval('catalogue')),
        })
    catalogue_to_location = fields.Many2One('stock.location', 'To Location',
        domain=[
            ('type', '=', 'storage'),
        ], states={
            'required': Bool(Eval('catalogue')),
        })
    catalogues = fields.Many2Many('res.user-stock.location.catalogue', 'user',
        'catalogue', 'Catalogues')

    @classmethod
    def __setup__(cls):
        super(User, cls).__setup__()
        cls._context_fields.insert(0, 'catalogues')
        cls._context_fields.insert(0, 'catalogue_from_location')
        cls._context_fields.insert(0, 'catalogue_to_location')


class UserCatalogue(ModelSQL, ModelView):
    'User - Catalogue'
    __name__ = 'res.user-stock.location.catalogue'
    user = fields.Many2One('res.user', 'User', ondelete='CASCADE',
        required=True)
    catalogue = fields.Many2One('stock.location.catalogue', 'Catalogue',
        ondelete='CASCADE', required=True)
