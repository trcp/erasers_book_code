distances = [1.2, -1.0, 0.8, 0.2, 1.5]   # -1.0 は測定に失敗した値
for d in distances:
    if d < 0:
        continue          # 失敗した値は飛ばす
    if d < 0.3:
        print(f"{d} m: 障害物が近いので停止")
        break             # 繰り返しを終了する
    print(f"{d} m: 前進")
