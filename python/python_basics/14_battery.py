battery = 12.6
minutes = 0
while battery > 11.0:
    battery -= 0.2      # 1 分ごとに 0.2 V 下がるとする
    minutes += 1
print(f"{minutes} 分で充電が必要になります")
