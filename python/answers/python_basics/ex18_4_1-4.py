# 練習問題 18.4 (1)
a = float(input("a => "))
b = float(input("b => "))
if a > b:
    print("a の方が大きい")
elif a < b:
    print("b の方が大きい")
else:
    print("a と b は同じ")

# 練習問題 18.4 (2)
height = float(input("身長 [m] => "))
weight = float(input("体重 [kg] => "))
bmi = weight / height ** 2
print(f"BMI = {bmi:.1f}")
if bmi < 18.5:
    print("やせ")
elif bmi < 25:
    print("標準")
elif bmi < 30:
    print("肥満")
else:
    print("高度肥満")

# 練習問題 18.4 (3)
num = int(input("整数 => "))
if num % 2 == 0:
    print("偶数である")
    if num >= 25:
        print("25 以上である")
if num % 3 == 0:
    print("3 の倍数である")

# 練習問題 18.4 (4)
voltage = float(input("電圧 [V] => "))
if voltage <= 0 or voltage > 15:
    print("センサの値が異常です")
elif voltage >= 12.0:
    print("充電十分")
elif voltage >= 11.0:
    print("そろそろ充電")
else:
    print("すぐに充電してください")
