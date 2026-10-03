import random


class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):
        print(f"{self.name}は攻撃をした！")


# 練習問題 19.2 (1)
class Wizard(Player):
    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self.mp = mp

    def magic(self):
        if self.mp < 10:
            print("魔力が足りない")
            return
        self.mp -= 10
        print(f"{self.name}は魔法を唱えた！（残り魔力: {self.mp}）")


wizard = Wizard("魔法使い", 60, 25)
wizard.attack()
wizard.magic()
wizard.magic()
wizard.magic()


# 練習問題 19.2 (2)
class Sensor:
    def __init__(self, name):
        self.name = name

    def read(self):
        return 0.0


class DummyLidar(Sensor):
    def read(self):
        return random.uniform(0.1, 5.0)


lidar = DummyLidar("lidar")
print(f"{lidar.name}: {lidar.read():.2f} m")
