import csv

import requests

from .metal import Metal


class Stock(Metal):
    type_name = 'stock'

    def get_current_price_per_unit(self):
        """ flask.pc5bai.com から最新の株買取単価を得る """
        url = f'http://flask.pc5bai.com/stock/info/csv'
        response = requests.get(url)
        reader = csv.DictReader(response.text.splitlines())
        for row in reader:
            if row['company_name'] == self.name:
                return int(row['buy'])
        raise NotImplementedError

    def sell(self, units):
        """ units 相当を売却する """
        url = 'https://flask.pc5bai.com/stock/api/buy/'
        data = {
            "name": self.name,
            "amount": units,
            "email": "foo@bar.com",
            "user": "山田太郎"
        }
        response = requests.post(url, json=data, )  # headers={'Content-Type': 'application/json'})
        if response.status_code != 200:
            raise Exception('売却に失敗しました。')
        self.amount -= units
        self.total_price -= self.get_current_price_per_unit() * units
        return response.json()['price']
