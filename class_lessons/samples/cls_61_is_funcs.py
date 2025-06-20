class Asset:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Metal(Asset):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight


jp_fund = Asset('日本国債', 1500)
us_fund = Asset('米国債', 2000)
silver = Metal('silver', 2000, 100)
gold = Metal('gold', 1000, 50)

print(isinstance(jp_fund, Asset))
print(isinstance(silver, Asset))

print(issubclass(silver.__class__, Metal))
print(issubclass(Metal, Asset))
