class Metal:
    asset_type = '貴金属'

    @classmethod
    def get_asset_type(cls):
        return cls.asset_type

    @classmethod
    def set_asset_type(cls, asset_type):
        cls.asset_type = asset_type

    def __init__(self, type_name, base_price, weight):
        self.type_name = type_name
        self.total_weight = weight
        self.total_price = base_price * weight


silver = Metal('silver', 2000, 100)

print(Metal.get_asset_type())
print(silver.get_asset_type())

Metal.set_asset_type('地金')

print(Metal.get_asset_type())
print(silver.get_asset_type())
