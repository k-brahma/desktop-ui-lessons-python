class Metal:
    asset_type = "貴金属"

    @classmethod
    def get_asset_type(cls):
        return cls.asset_type

    @classmethod
    def set_asset_type(cls, new_asset_type):
        cls.asset_type = new_asset_type

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
print(Metal.get_asset_type())

Metal.set_asset_type('地金')

print(Metal.asset_type)
print(Metal.get_asset_type())

print("終了しました")
