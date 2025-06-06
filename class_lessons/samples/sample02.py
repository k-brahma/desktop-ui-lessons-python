class Metal:
    def __init__(self, type_name, amount, total_price):
        self.type_name = type_name
        self.amount = amount
        self.total_price = total_price

    def get_per_unit_price(self):
        """ 1グラムあたりの価格を返す """
        return self.total_price / self.amount

    def add(self, new_amount, new_total_price):
        """ 追加で入手した金属の重さと価格を追加する """
        self.amount += new_amount
        self.total_price += new_total_price


my_metal = Metal('silver', 100, 15000)
print(my_metal.type_name, my_metal.total_price, my_metal.amount)
print(my_metal.get_per_unit_price())

my_metal.add(200, 20000)
print(my_metal.type_name, my_metal.total_price, my_metal.amount)
print(my_metal.get_per_unit_price())

print("終了しました")
