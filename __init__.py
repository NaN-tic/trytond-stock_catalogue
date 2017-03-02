# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
import location
import user


def register():
    Pool.register(
        location.Catalogue,
        location.CatalogueLines,
        user.User,
        module='stock_catalogue', type_='model')
