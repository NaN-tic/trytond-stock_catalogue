# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval, Bool

__all__ = ['User', 'UserCatalogue']
__metaclass__ = PoolMeta


class User:
    __name__ = 'res.user'

    @classmethod
    def __setup__(cls):
        super(User, cls).__setup__()
        cls._context_fields.insert(0, 'catalogues')

    catalogue = fields.Many2One('stock.location.catalogue', 'Catalogue')
    from_location = fields.Many2One('stock.location', 'From Location',
        domain=[
            ('type', 'in', ['view', 'storage']),
        ], states={
            'required': Bool(Eval('catalogue')),
        })

    location = fields.Many2One('stock.location', 'Location',
        domain=[
            ('type', '=', 'storage'),
        ], states={
            'required': Bool(Eval('catalogue')),
        })
    catalogues = fields.Many2Many('res.user-stock.location.catalogue', 'user',
        'catalogue', 'Catalogues')


class UserCatalogue(ModelSQL, ModelView):
    'User - Catalogue'
    __name__ = 'res.user-stock.location.catalogue'

    user = fields.Many2One('res.user', 'User', ondelete='CASCADE',
        required=True, select=True)
    catalogue = fields.Many2One('stock.location.catalogue', 'Catalogue',
        ondelete='CASCADE', required=True, select=True)
