from .metal import Metal
from .mixins import CSVDealsMixin


class WrappedStock(CSVDealsMixin, Metal):
    name = 'stock'

    def get_current_price_per_unit(self):
        return self.get_current_price_per_unit_from_csv()
