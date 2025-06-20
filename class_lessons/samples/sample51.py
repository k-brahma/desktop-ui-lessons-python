class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def jikoshokai(self):
        return f'はじめまして！私は｛self.name｝です！'


if __name__ == '__main__':
    h = Human("山田太郎", 20)
    print(h.name)
    print(h.age)

    print(h.jikoshokai())
