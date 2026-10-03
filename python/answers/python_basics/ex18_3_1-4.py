# 練習問題 18.3 (1)
colors = ["green", "blue", "red", "black", "white"]
print(colors[1:4])

# 練習問題 18.3 (2)
members = ["satou", "tanaka", "suzuki"]
members.append("itou")
members.remove("satou")
print(members)       # ['tanaka', 'suzuki', 'itou']
print(members[1])    # suzuki

# 練習問題 18.3 (3)
heights = [176, 158, 164]
print(sum(heights) / len(heights))   # 166.0

# 練習問題 18.3 (4)
robot = {"name": "turtle", "max_speed": 0.5}
robot["max_speed"] = 0.8
robot["battery"] = 12.0
print(f"{robot['name']} の最高速度は {robot['max_speed']} m/s")
