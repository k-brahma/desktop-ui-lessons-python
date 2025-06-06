import csv

import requests

from sample41 import BaseAsset


class CSVMixin:
    """
    csvファイルを解析する mixin クラス
    """

    def get_value_from_csv(self, response, field_no):
        """
        csvファイルを取得して、key に対応する値を返す
        """
        text_lines = response.text.splitlines()
        reader = csv.reader(text_lines, )
        for row in reader:
            if row[0] == self.type_name:
                return int(row[field_no])
        return None


class Stock(CSVMixin, BaseAsset):
    allowed_types = ['toggle', 'orange', 'macrosoft', 'nile', ]
    asset_type = "株券"
    base_url = 'https://flask.pc5bai.com/stock/'

    def __init__(self, type_name, total_price, amount, date='', trader=''):
        super().__init__(type_name, total_price, amount, )

        self.date = date
        self.trader = trader

    def get_current_unit_price(self):
        """ 現在の買取単価を調べる """
        url = f'{self.base_url}/info/csv/'
        response = requests.get(url)
        if response.status_code != 200:
            return None
        return self.get_value_from_csv(response, 1)


if __name__ == '__main__':
    ms = Stock("macrosoft", 600000, 3000, date='2022-10-19', trader='G証券')
    print(ms.get_current_unit_price())

   #  result = isinstance(ms, Stock)
   #  print(result)
   #
   #  result = isinstance(ms, BaseAsset)
   #  print(result)
   #
   #  result = isinstance(ms, CSVMixin)
   #  print(result)
   #
   #  result = issubclass(Stock, BaseAsset)
   #  print(result)
   #
   #  result = issubclass(Stock, CSVMixin)
   #  print(result)
