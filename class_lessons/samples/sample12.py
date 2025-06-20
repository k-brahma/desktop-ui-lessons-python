class Metal:
    def __init__(self, type_name, base_price, amount, **kwargs):
        self.type_name = type_name
        self.total_price = base_price * amount
        self.amount = amount

        for key, value in kwargs.items():
            setattr(self, key, value)

        print('ひととおりの引数を処理し終えました')

    def get_per_unit_price(self):
        return self.total_price / self.amount


silver = Metal("silver", 6000, 120, date="2022-10-18",
               store="ガラパゴス金属横浜支店", memo="担当K氏",
               origin_county="アルゼンチン", )

print(silver.type_name)
print(silver.date)
print(silver.origin_county)
