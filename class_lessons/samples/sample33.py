import csv

import requests

from sample31 import Metal


class NewStock(Metal):
    """
    Metalを継承して作ったクラス
    """

    allowed_types = ['toggle', 'orange', 'macrosoft', 'nile', ]
    asset_type = "株券"
    base_url = 'https://flask.pc5bai.com/stock/'

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


if __name__ == '__main__':
    ms = NewStock("macrosoft", 600000, 3000)
    print(ms.get_current_unit_price())
    print(ms.get_current_price(1000))
    print(ms.get_current_total_price())

    price = ms.execute_sell(1000)
    print(price)
    print(ms.amount)

    orange = NewStock("orange", 140000, 1000)
    print(orange.get_current_unit_price())
    print(orange.get_current_total_price())
