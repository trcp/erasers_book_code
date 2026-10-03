class Robot:
    def __init__(self, name, max_speed=0.5):
        self.name = name
        self.max_speed = max_speed
        self.x = 0.0
        self.battery = 100

    def move(self, speed, duration):
        if self.battery <= 0:
            print("バッテリ切れです")
            return
        if speed > self.max_speed:
            speed = self.max_speed
        distance = speed * duration
        self.x += distance
        self.battery -= distance * 10
        print(f"x = {self.x:.2f} m, バッテリ {self.battery:.0f}%")


robot = Robot("turtle")
for i in range(12):
    robot.move(0.5, 2.0)
