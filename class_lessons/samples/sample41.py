import json

import requests


class BaseAsset:
    allowed_types = []
    asset_type = ""
    base_url = ''

    def __init__(self, type_name, total_price, amount, **kwargs):
        if type_name not in self.allowed_types:
            raise ValueError(f'許可されていない商品です: {type_name}')
        self.type_name = type_name
        self.total_price = total_price
        self.amount = amount

    def __str__(self):
        return f'{self.type_name} {self.amount}g'

    def get_per_unit_price(self):
        return self.total_price / self.amount

    def get_current_unit_price(self):
        """ 現在の買取単価を調べる """
        # return NotImplemented
        raise NotImplementedError

    def get_current_price(self, amount):
        """ 指定された分だけ売った場合の買い取り価格を返す """
        return self.get_current_unit_price() * amount

    def get_current_total_price(self):
        return self.get_current_unit_price() * self.amount

    def execute_sell(self, amount):
        """ 指定された分だけ買い取りをしてもらう
            戻り値は、売れた金額
            手元の金属の量も減る """
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


if __name__ == '__main__':
    BaseAsset.allowed_types = ['日本国債', ]
    jp_bond = BaseAsset('日本国債', 10000, 1000)
    result = jp_bond.get_current_unit_price()
    # print(result)
