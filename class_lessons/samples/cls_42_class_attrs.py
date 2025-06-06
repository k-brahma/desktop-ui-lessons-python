"""
クラス変数は、クラスに直接アクセスすると変更できる。

一方、インスタンスで同名の変数を定義することができる。
インスタンスで同名の変数を定義した場合、インスタンスからは、同名のクラス変数に簡単にはアクセスできなくなる。
(不可能ではない)
"""


class Metal:
    asset_type = '貴金属'

    def __init__(self, type_name, base_price, amount):
        self.type_name = type_name
        self.amount = amount
        self.total_price = base_price * amount


silver = Metal('silver', 2000, 100)
platinum = Metal('platinum', 3000, 50)

print(Metal.asset_type)
print(silver.asset_type)
print(platinum.asset_type)

# platinum インスタンスの type 属性を新たに設定(クラスの type 属性ではないので注意！)
platinum.asset_type = 'プラチナ'

print(Metal.asset_type)
print(silver.asset_type)
print(platinum.asset_type)

# クラスの type 属性を変更
Metal.asset_type = '地金'

print(Metal.asset_type)
print(silver.asset_type)
print(platinum.asset_type)  # gold.type_name は gold インスタンスの type 属性 なので 'stock'
print(platinum.__class__.asset_type)  # クラスの type 属性を参照するのに# __class__ を使った
