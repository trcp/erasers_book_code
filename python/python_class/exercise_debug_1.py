# 練習問題：誤りを探して直すプログラム（このままでは正しく動かない）
import random

while True:
    num = random.randint(1, 10)
    print("生成された乱数:" + str(num))
    if num == 5:
        break

print("生成された乱数:" + str(num))
