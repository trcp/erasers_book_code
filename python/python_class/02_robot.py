class Robot:
    def __init__(self, name, max_speed=0.5):
        self.name = name
        self.max_speed = max_speed
        self.x = 0.0

    def move(self, speed, duration):
        # 最高速度を超えないように制限する
        if speed > self.max_speed:
            speed = self.max_speed
        self.x += speed * duration
        print(f"{self.name}: {speed} m/s で {duration} 秒進んだ（x = {self.x:.2f}）")


robot = Robot("turtle")
robot.move(0.3, 2.0)
robot.move(1.0, 2.0)   # 最高速度 0.5 m/s に制限される
