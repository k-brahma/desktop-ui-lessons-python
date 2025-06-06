class Asset:
    """ 資産クラス """
    type_name = 'asset'

    def __init__(self, name, total_price, ):
        self.name = name
        self.total_price = total_price

    def __str__(self):
        return f'{self.name} {self.total_price}'

    def __add__(self, other):
        return self.total_price + other.total_price

    def __eq__(self, other):
        return self.total_price == other.total_price

    def get_total_price(self):
        return self.total_price

    def get_info(self):
        return f'{self.name}を総額{self.total_price:,}円有しています。'
