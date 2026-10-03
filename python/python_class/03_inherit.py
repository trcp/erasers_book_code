class Robot:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"こんにちは、{self.name}です")

    def move(self):
        print(f"{self.name}は移動した")


class DroneRobot(Robot):   # Robot クラスを継承する
    def __init__(self, name, max_height):
        super().__init__(name)          # 親クラスの __init__ を呼ぶ
        self.max_height = max_height    # 子クラスで属性を追加する

    def move(self):                     # 親クラスのメソッドを上書きする
        print(f"{self.name}は高度 {self.max_height} m まで飛んだ")


drone = DroneRobot("tello", 10)
drone.hello()    # 親クラスから引き継いだメソッド
drone.move()     # 子クラスで上書きしたメソッド
