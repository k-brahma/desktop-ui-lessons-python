class Metal:
    def __init__(self, type_name, amount, base_price, **kwargs):
        self.type_name = type_name
        self.amount = amount
        self.total_price = base_price * amount

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __call__(self, *args, **kwargs):
        return f'{self.type_name} を {self.total_price:,} 円相当有しています'

    def get_per_unit_price(self):
        return self.total_price / self.amount


silver = Metal('silver', 2000, 100, date='2022-10-14',
               origin_country='Argentina', store='ガラパゴス貴金属',
               memo='担当K氏')

print(silver.type_name)
print(silver.amount)
print(silver.total_price)

print(silver.date)
print(silver.origin_country)
print(silver.store)
print(silver.memo)
