import requests

from .asset import Asset


class Metal(Asset):
    type_name = 'metal'

    def __init__(self, name, base_price, amount):
        super().__init__(name, base_price * amount)
        self.amount = amount

    def get_info(self):
        return f'{self.name} {self.amount}グラム 総額{self.total_price:,}円有しています。'

    def get_price_per_unit(self):
        """ 購入単価を返す """
        return self.total_price / self.amount

    def get_current_price_per_unit(self):
        """ flask.pc5bai.com から最新の貴金属買取単価を得る """
        url = f'https://flask.pc5bai.com/metal/api/info/{self.name}'
        response = requests.get(url)
        return response.json()['buy']

    def get_current_total_price(self):
        return self.get_current_price_per_unit() * self.amount

    def sell(self, units):
        """ units 相当を売却する """
        url = 'https://flask.pc5bai.com/metal/api/buy/'
        data = {"name": self.name, "amount": units, "email": "foo@bar.com", "user": "山田太郎"
                }
        response = requests.post(url, json=data, )
        if response.status_code != 200:
            raise Exception('売却に失敗しました。')
        self.amount -= units
        self.total_price -= self.get_current_price_per_unit() * units
        return response.json()['price']
