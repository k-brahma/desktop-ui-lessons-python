class Metal:
    asset_type = "貴金属"

    def __init__(self, type_name, base_price, amount, ):
        self.type_name = type_name
        self.total_price = base_price * amount
        self.amount = amount
        print('ひととおりの引数を処理し終えました')

    def get_per_unit_price(self):
        return self.total_price / self.amount


silver = Metal("silver", 6000, 120)
platinum = Metal("platinum", 9000, 150)
print(Metal.asset_type)
print(silver.type_name)
print(platinum.type_name)

Metal.asset_type = "貴金属（変更）"
print(Metal.asset_type)
print(silver.asset_type)
print(platinum.asset_type)

silver.asset_type = "私の銀の延べ棒"
print(Metal.asset_type)
print(silver.asset_type)
print(platinum.asset_type)

print("終了しました")
