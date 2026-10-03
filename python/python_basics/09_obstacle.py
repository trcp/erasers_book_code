distance = float(input("障害物までの距離 [m] => "))

if distance < 0.3:
    print("停止します")
elif distance < 1.0:
    print("減速します")
else:
    print("そのまま進みます")
