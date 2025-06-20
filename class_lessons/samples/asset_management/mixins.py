import csv

import requests


class CSVDealsMixin:
    """ 株取引のためのメソッドを有する、多重継承用のクラス """

    def __init__(self, name, base_price, amount):
        self.name=name
        self.total_price = base_price * amount
        self.amount = amount

    def get_info(self):
        return f'{self.name} {self.amount}株 総額{self.total_price:,}円有しています。'

    def get_price_per_unit(self):
        """ 購入単価を返す """
        return self.total_price / self.amount

    def get_csv_deals(self):
        url = f'http://flask.pc5bai.com/stock/info/csv'
        response = requests.get(url)
        return response.text.splitlines()

    def get_current_price_per_unit_from_csv(self):
        """
        flask.pc5bai.com から最新の株買取単価を得る
        """
        reader = csv.DictReader(self.get_csv_deals())
        for row in reader:
            if row['company_name'] == self.name:
                return int(row['buy'])
        raise NotImplementedError

    def sell(self, units):
        """ units 相当を売却する """
        url = 'https://flask.pc5bai.com/stock/api/buy/'
        data = {"name": self.name, "amount": units, "email": "foo@bar.com", "user": "山田太郎"
                }
        response = requests.post(url, json=data, )
        if response.status_code != 200:
            raise Exception('売却に失敗しました。')
        self.amount -= units
        self.total_price -= self.get_current_price_per_unit_from_csv() * units
        return response.json()['price']
