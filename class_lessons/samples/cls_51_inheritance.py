from asset_management.asset import Asset
from asset_management.metal import Metal
from asset_management.stock import Stock

if __name__ == '__main__':
    jp_bond = Asset('日本国債', 1000000)
    print(jp_bond)
    print(jp_bond.get_info())
    print(jp_bond.get_total_price())

    gold = Metal('gold', 50000, 1000)
    print(gold)
    print(gold.get_info())
    print(gold.get_total_price())
    print(gold.get_price_per_unit())
    print(gold.get_current_price_per_unit())
    print(gold.get_current_total_price())

    # 一部を売る
    result = gold.sell(100)
    print(result)
    print(gold)
    print(gold.get_info())
    print(gold.get_total_price())

    orange = Stock('orange', 12000, 500)
    print(orange)
    print(orange.get_info())
    print(orange.get_price_per_unit())
    print(orange.get_current_price_per_unit())
    print(orange.get_current_total_price())

    # 一部を売る
    result = orange.sell(150)
    print(result)
    print(orange)
    print(orange.get_info())
    print(orange.get_total_price())

    print('終了しました')
