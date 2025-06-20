import csv
import json

import requests


class Stock:
    allowed_types = ['toggle', 'orange', 'macrosoft', 'nile', ]
    asset_type = "株券"
    base_url = 'https://flask.pc5bai.com/stock/'

    def __init__(self, type_name, total_price, amount):
        if type_name not in self.allowed_types:
            raise ValueError(f'許可されていない商品です: {type_name}')
        self.type_name = type_name
        self.total_price = total_price
        self.amount = amount

    def __str__(self):
        return f'{self.type_name} {self.amount}株'

    def get_per_unit_price(self):
        return self.total_price / self.amount

    def get_current_unit_price(self):
        """ 現在の買取単価を調べる """
        url = f'{self.base_url}/info/csv/'
        response = requests.get(url)
        if response.status_code != 200:
            return None
        text_lines = response.text.splitlines()
        reader = csv.reader(text_lines, )
        for row in reader:
            if row[0] == self.type_name:
                return int(row[1])
        return None

    def get_current_price(self, amount):
        """ 指定された分だけ売った場合の買い取り価格を返す """
        return self.get_current_unit_price() * amount

    def get_current_total_price(self):
        return self.get_current_unit_price() * self.amount

    def execute_sell(self, amount):
        """ 指定された分だけ売る """
        if amount > self.amount:
            raise ValueError(f'手持ちの財産より多い量は指定できません: {self.amount}, {amount}')

        url = f'{self.base_url}/api/buy/'
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": self.type_name,
            "amount": amount,
            "email": "foo@bar.com",
            "user": "山田太郎",
        }
        response = requests.post(url, data=json.dumps(data), headers=headers, )
        if response.status_code != 200:
            return None
        result_dict = response.json()
        price = result_dict['price']
        self.amount -= amount
        return price


# bodybook = Stock('bodybook', 100000, 100)

ms = Stock("macrosoft", 600000, 3000)
print(ms.get_current_unit_price())
print(ms.get_current_price(1000))
print(ms.get_current_total_price())

price = ms.execute_sell(1000)
print(price)
print(ms.amount)

orange = Stock("orange", 140000, 1000)
print(orange.get_current_unit_price())
print(orange.get_current_total_price())
