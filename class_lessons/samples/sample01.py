class Metal:
    def __init__(self, type_name, amount, total_price):
        self.type_name = type_name
        self.amount = amount
        self.total_price = total_price

    def get_per_unit_price(self):
        """ 1グラムあたりの価格を返す """
        return self.total_price / self.amount


my_metal = Metal('silver', 100, 15000)
print(my_metal.type_name, my_metal.total_price, my_metal.amount)

gold = Metal('gold', 100, 20000)
print(gold.type_name, gold.total_price, gold.amount)

platinum = Metal('platinum', 100, 30000)
print(platinum.type_name, platinum.total_price, platinum.amount)

print("終了しました")
