class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name_and_age(self):
        return f'{self.name} {self.age}'


if __name__ == '__main__':
    h = Human("山田太郎", 20)
    print(h.name)
    print(h.age)

    print(h.name_and_age)

    h.name = "田中花子"
    print(h.name_and_age)

    # h.name_and_age = "ほげほげ治郎 30"
