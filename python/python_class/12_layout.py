# 1. import
import math

# 2. 定数
WHEEL_RADIUS = 0.033   # 車輪の半径 [m]


# 3. 関数・クラスの定義
def wheel_speed(rps):
    return 2 * math.pi * WHEEL_RADIUS * rps


# 4. 実行する処理
if __name__ == "__main__":
    print(wheel_speed(2.0))
