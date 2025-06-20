class Metal:
    def __init__(self, type_name, base_price, amount):
        self.type_name = type_name
        self.amount = amount
        self.total_price = base_price * amount

    def get_per_unit_price(self):
        return self.total_price / self.amount


silver = Metal('silver', 6000, 120)

print(hasattr(silver, 'type_name'))
print(hasattr(silver, 'company_name'))

print(getattr(silver, 'type_name'))
# print(getattr(silver, 'company_name'))
print(getattr(silver, 'company_name', '購入元不明'))

setattr(silver, 'company_name', 'ガラパゴス貴金属')
print(getattr(silver, 'company_name'))

delattr(silver, 'company_name')
print(hasattr(silver, 'company_name'))

silver.date = '2020/01/01'
print(silver.date)

silver.amount = 150
print(silver.amount)

# print(silver.origin_country) #存在しないのでエラー

# プロパティだけでなく、メソッドも取得できる。使うことはまずないが、紹介。
method = silver.get_per_unit_price
print(method())
