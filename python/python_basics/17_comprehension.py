distances = [1.2, -1.0, 0.8, 0.2, 1.5]

distances_cm = [d * 100 for d in distances]
print(distances_cm)   # [120.0, -100.0, 80.0, 20.0, 150.0]

valid = [d for d in distances if d >= 0]   # 正しく測れた値だけ
print(valid)          # [1.2, 0.8, 0.2, 1.5]
print(min(valid))     # 一番近い障害物までの距離 0.2
