class Metal:
    def get_per_unit_price(self):
        """ 1グラムあたりの価格を返す """
        return self.total_price / self.amount

    def add(self, new_amount, new_total_price):
        """ 追加で入手した金属の重さと価格を追加する """
        self.amount += new_amount
        self.total_price += new_total_price

    def __init__(self, type_name, amount, total_price):
        self.type_name = type_name
        self.amount = amount
        self.total_price = total_price

    def __call__(self, ):
        """ インスタンスを関数のように呼び出すときに使う """
        return f'{self.get_per_unit_price()}円相当の{self.type_name}を有しています'

    def __str__(self):
        """ str() 関数の引数になったときに呼び出される """
        return f"{self.type_name} {self.amount}g {self.total_price}円"

    def __repr__(self):
        """ repr() 関数の引数になったときに呼び出される """
        return f"Metal({self.type_name}, {self.amount}, {self.total_price})"

    def __add__(self, other):
        return self.total_price + other.total_price

    def __sub__(self, other):
        return self.total_price - other.total_price

    def __eq__(self, other):
        if self.total_price != other.total_price:
            return False
        if self.type_name != other.type_name:
            return False
        return True


my_metal = Metal('platinum', 100, 35000)
gold = Metal('platinum', 200, 35000)

str_result_1 = str(my_metal)
str_result_2 = my_metal.__str__()

repr_result_1 = repr(my_metal)
repr_result_2 = my_metal.__repr__()

total_metal_price_1 = my_metal + gold
total_metal_price_2 = my_metal.__add__(gold)

minus_result = my_metal - gold
print(minus_result)

eq_result_1 = my_metal == gold
eq_result_2 = my_metal.__eq__(gold)
print(eq_result_1, eq_result_2)

print("終了しました")
