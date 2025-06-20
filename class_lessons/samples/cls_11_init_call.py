class Metal:
    def get_per_unit_price(self):
        """ 1グラムあたりの価格を返す """
        return self.total_price / self.amount

    def __init__(self, type_name, amount, total_price):
        self.type_name = type_name
        self.amount = amount
        self.total_price = total_price

    def __call__(self, ):
        """ インスタンスを関数のように呼び出すときに使う """
        return f'{self.get_per_unit_price()}円相当の{self.type_name}を有しています'


my_metal = Metal('platinum', 100, 35000)

call_result = my_metal()
print(call_result)

print("終了しました")
