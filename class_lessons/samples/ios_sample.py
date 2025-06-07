class IOSDevice:
    os = None  # os
    year = None  # 発売日
    storage_size = None  # ストレージサイズ単位はGB
    type_name = ""  # 型名
    is_tablet = False  # True のとき iPhone
    owner_name = ""

    def __init__(self, owner_name, type_name):
        self.owner_name = owner_name
        self.type_name = type_name

    def show_info(self):
        return f"{self.owner_name}さんの{self.type_name}です"


class IPhone(IOSDevice):
    os = "iOS 16.5"
    year = 2016
    storage_size = 128
    is_tablet = False


class Tablet(IOSDevice):
    os = "iOS 20.5"
    year = 2020
    storage_size = 512
    type_name = "tablet"
    is_tablet = True


itoke_no_phone = IPhone("伊藤", "iPhone10")
print(itoke_no_phone.show_info())

ogawa_no_iphone = IPhone("小川", "iPhone8")
print(ogawa_no_iphone.show_info())

ogawa_no_ipad_mini = Tablet("田中", "iPad mini")
print(ogawa_no_ipad_mini.show_info())
