import unittest
from decimal import Decimal

from proteus import Model
from trytond.modules.company.tests.tools import create_company
from trytond.tests.test_tryton import drop_db
from trytond.tests.tools import activate_modules


class Test(unittest.TestCase):

    def setUp(self):
        drop_db()
        super().setUp()

    def tearDown(self):
        drop_db()
        super().tearDown()

    def test(self):

        # Install stock_catalogue
        activate_modules('stock_catalogue')

        # Create company
        _ = create_company()

        # Create product
        ProductUom = Model.get('product.uom')
        ProductTemplate = Model.get('product.template')
        unit, = ProductUom.find([('name', '=', 'Unit')])
        template = ProductTemplate()
        template.name = 'Product1'
        template.default_uom = unit
        template.type = 'goods'
        template.list_price = Decimal('20')
        template.save()
        product1, = template.products
        template = ProductTemplate()
        template.name = 'Product2'
        template.default_uom = unit
        template.type = 'goods'
        template.list_price = Decimal('20')
        template.save()
        product2, = template.products
        template = ProductTemplate()
        template.name = 'Product3'
        template.default_uom = unit
        template.type = 'goods'
        template.list_price = Decimal('20')
        template.save()
        product3, = template.products

        # Get stock locations
        Location = Model.get('stock.location')
        storage_loc, = Location.find([('code', '=', 'STO')])

        # Create catalogue
        Catalogue = Model.get('stock.location.catalogue')
        CatalogueLine = Model.get('stock.location.catalogue.line')
        catalogue = Catalogue()
        catalogue.name = 'DEMO'
        catalogue.location = storage_loc
        catalogue_line = CatalogueLine()
        catalogue.lines.append(catalogue_line)
        catalogue_line.product = product1
        catalogue_line.max_quantity = 12
        catalogue_line = CatalogueLine()
        catalogue.lines.append(catalogue_line)
        catalogue_line.product = product2
        catalogue_line.max_quantity = 5
        catalogue_line = CatalogueLine()
        catalogue.lines.append(catalogue_line)
        catalogue_line.product = product3
        catalogue_line.max_quantity = 15
        catalogue.save()
