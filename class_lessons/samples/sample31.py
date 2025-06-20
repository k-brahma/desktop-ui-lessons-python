import json

import requests


class Metal:
    allowed_types = ['silver', 'gold', 'platinum', ]
    asset_type = "貴金属"
    base_url = 'https://flask.pc5bai.com/metal/'

    def __init__(self, type_name, total_price, amount, ):
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
        url = f'{self.base_url}/api/info/{self.type_name}/'
        response = requests.get(url)
        if response.status_code != 200:
            return None
        result_dict = response.json()
        return result_dict['buy']

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
    # hg = Metal("水銀", 100000, 100)
    # hg.get_current_unit_price()
    # hg.get_current_price(5)

    silver = Metal("silver", 6000, 120)
    print(silver)

    # price = silver.execute_sell(30000)
    # print(price)

    print(silver.amount)

    print(silver.amount)
    print(silver.get_current_total_price())

    price = silver.execute_sell(100)
    print(f'{price:,}円')

    print(silver.amount)
    print(silver.get_current_total_price())

    print("ここからプラチナ")

    platinum = Metal("platinum", 9000, 150)
    print(platinum)

    print(platinum.get_per_unit_price())
    print(platinum.get_current_total_price())

    print(platinum.execute_sell(50))

    print(platinum.amount)
    print(platinum.get_current_total_price())
