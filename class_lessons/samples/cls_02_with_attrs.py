class Metal:
    type_name = "silver"
    total_price = 10000
    amount = 2000

    def get_per_unit_price(self):
        """ 1グラムあたりの単価を返す """
        return self.total_price / self.amount


my_silver = Metal()

print(my_silver.amount, my_silver.total_price)

result = my_silver.get_per_unit_price()
print(result)
