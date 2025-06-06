class Metal:
    type_name = "silver"
    total_price = 10000
    amount = 2000

    def get_per_unit_price(self):
        """ 1グラムあたりの単価を返す """
        return self.total_price / self.amount

    def add(self, price, new_amount):
        """ 追加で入手した貴金属の情報を組み入れる """
        self.total_price += price
        self.amount += new_amount


my_silver = Metal()

print(my_silver.amount, my_silver.total_price)

result = my_silver.get_per_unit_price()
print(result)

my_silver.add(price=10000, new_amount=3000)

print(my_silver.amount, my_silver.total_price)

result = my_silver.get_per_unit_price()
print(result)
