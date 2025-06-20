import requests

from sample41 import BaseAsset


class Metal(BaseAsset):
    allowed_types = ['silver', 'gold', 'platinum', ]
    asset_type = "貴金属"
    base_url = 'https://flask.pc5bai.com/metal/'

    def get_current_unit_price(self):
        """ 現在の買取単価を調べる """
        url = f'{self.base_url}/api/info/{self.type_name}/'
        response = requests.get(url)
        if response.status_code != 200:
            return None
        result_dict = response.json()
        return result_dict['buy']


if __name__ == '__main__':
    # hg = Metal("水銀", 100000, 100)
    # hg.get_current_unit_price()
    # hg.get_current_price(5)

    silver = Metal("silver", 6000, 120)
    print(silver)

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

    # result = isinstance(silver, Metal)
    # print(result)
    #
    # result = isinstance(silver, BaseAsset)
    # print(result)
    #
    # result = isinstance(silver, object)
    # print(result)
    #
    # result = isinstance(silver, int)
    # print(result)
    #
    # subclass_result = issubclass(Metal, BaseAsset)
    # print(subclass_result)
    #
    # subclass_result = issubclass(Metal, object)
    # print(subclass_result)
    #
    # subclass_result = issubclass(Metal, int)
    # print(subclass_result)

    # price = silver.execute_sell(30000)
    # print(price)
