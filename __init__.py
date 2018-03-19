# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from . import location
from . import user


def register():
    Pool.register(
        location.Catalogue,
        location.CatalogueLines,
        user.User,
        user.UserCatalogue,
        module='stock_catalogue', type_='model')
