class Metal:
    asset_type = "貴金属"

    def __init__(self, type_name, base_price, amount, ):
        self.type_name = type_name
        self.total_price = base_price * amount
        self.amount = amount
        print('ひととおりの引数を処理し終えました')

    def get_per_unit_price(self):
        return self.total_price / self.amount


print(Metal.asset_type)
silver = Metal("silver", 6000, 120)
print(silver.type_name)

print("終了しました")
