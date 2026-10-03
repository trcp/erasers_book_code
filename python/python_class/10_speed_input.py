while True:
    try:
        speed = float(input("速度 [m/s] => "))
        break
    except ValueError:
        print("数値を入力してください")
print(f"速度を {speed} m/s に設定しました")
