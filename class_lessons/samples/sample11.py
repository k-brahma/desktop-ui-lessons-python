class Metal:
    def __init__(self, type_name, base_price, amount):
        self.type_name = type_name
        self.total_price = base_price * amount
        self.amount = amount

    def get_per_unit_price(self):
        return self.total_price / self.amount


silver = Metal("silver", 6000, 120)

has_type_name = hasattr(silver, "type_name")
has_company_name = hasattr(silver, "company_name")

get_type_name_result = getattr(silver, "type_name")
get_company_name_result_1 = getattr(silver, "company_name", "会社名不明")

setattr(silver, "company_name", "ガラパゴス貴金属")
get_company_name_result_2 = getattr(silver, "company_name", )

delattr(silver, "company_name")
get_company_name_result_3 = getattr(silver, "company_name", "わかりません")

silver.date = "2022-10-18"
get_date_result_1 = getattr(silver, "date", "購入日不明")
get_date_result_2 = silver.date

print('終了しました')
