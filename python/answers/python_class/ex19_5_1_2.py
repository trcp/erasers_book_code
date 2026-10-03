import random

# 練習問題 19.5 (1)
for i in range(10):
    num = random.randint(0, 3)
    try:
        print(100 / num)
    except ZeroDivisionError:
        print("0 で割ろうとしました")

# 練習問題 19.5 (2)
try:
    num = int(input("整数を入力してください=> "))
except ValueError:
    num = 10
print(num + 100)
