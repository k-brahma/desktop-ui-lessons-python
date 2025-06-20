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


my_metal = Metal('silver', 100, 15000)

call_result = my_metal()
print(call_result)

str_result = str(my_metal)
print(str_result)

repr_result = repr(my_metal)
print(repr_result)

print("終了しました")
