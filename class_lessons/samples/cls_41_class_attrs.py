class Metal:
    asset_type = '貴金属'

    def __init__(self, type_name, base_price, amount):
        self.type_name = type_name
        self.amount = amount
        self.total_price = base_price * amount


print(Metal.asset_type)

silver = Metal('silver', 2000, 100)
platinum = Metal('platinum', 3000, 50)

print(silver.asset_type)
print(platinum.asset_type)
