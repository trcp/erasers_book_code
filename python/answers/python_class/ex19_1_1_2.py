# 練習問題 19.1 (1)
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"私の名前は{self.name}です")

    def show_age(self):
        print(f"年齢は{self.age}歳です")


john = Human("ジョン", 23)
marine = Human("マリン", 18)
john.introduce()
john.show_age()
marine.introduce()
marine.show_age()


# 練習問題 19.1 (2)
class Tax:
    def __init__(self, rate):
        self.rate = rate   # 税率 [%]

    def price(self, value):
        total = round(value * (1 + self.rate / 100))
        print(f"{value} 円（税率 {self.rate}%）→ {total} 円")


tax8 = Tax(8)
tax10 = Tax(10)
for value in [250, 580]:
    tax8.price(value)
    tax10.price(value)
