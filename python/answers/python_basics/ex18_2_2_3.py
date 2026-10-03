# 練習問題 18.2 (2)
title = input("アニメ名=> ")
print(f"{title}は{len(title)}文字です。")

# 練習問題 18.2 (3)
radius = float(input("車輪の半径 [m] => "))
rps = float(input("1 秒あたりの回転数 => "))
print(f"速さは {2 * 3.14 * radius * rps:.2f} m/s です")
