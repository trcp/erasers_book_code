distances = [1.2, -1.0, 0.8, 0.2, 1.5]   # [m]、-1.0 は測定に失敗した値
distances_cm = []
for d in distances:
    distances_cm.append(d * 100)
print(distances_cm)   # [120.0, -100.0, 80.0, 20.0, 150.0]
