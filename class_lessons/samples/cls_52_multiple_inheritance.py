from asset_management.asset import Asset
from asset_management.mixins import CSVDealsMixin


class WrappedStock(CSVDealsMixin, Asset):
    """ CSVDealsMixin, Asset を継承した、貴金属クラス """
    name = 'metal'

    def __init__(self, name, base_price, total_weight):
        super().__init__(name, base_price, total_weight)
        self.total_weight = total_weight

    def __str__(self):
        return f'{self.type_name} {self.total_price} {self.total_weight}'

    def get_info(self):
        return f'{self.type_name} {self.total_weight}グラム 総額{self.total_price:,}円有しています。'


if __name__ == '__main__':
    orange = WrappedStock('orange', 12000, 500)
    print(orange)
    print(orange.get_info())
    print(orange.get_price_per_unit())
    print(orange.get_current_price_per_unit_from_csv())
    print(orange.sell(3000))
