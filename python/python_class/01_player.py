class Player:
    def __init__(self, name, hp):
        self.name = name   # インスタンスごとのデータ（属性）
        self.hp = hp

    def attack(self):
        print(f"{self.name}は攻撃をした！")

    def heal(self, amount):
        self.hp += amount
        print(f"{self.name}の体力が {amount} 回復した（体力: {self.hp}）")


hero = Player("勇者", 100)      # インスタンスを作る
wizard = Player("魔法使い", 60)

hero.attack()
wizard.attack()
wizard.heal(20)
print(hero.hp, wizard.hp)
