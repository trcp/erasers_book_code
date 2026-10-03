params = {"name": "turtle", "max_speed": 0.5, "wheel_radius": 0.033}
print(params["max_speed"])     # キーで値を取り出す
params["max_speed"] = 0.3      # 値を変更する
params["use_lidar"] = True     # 新しいキーと値を追加する
print(params)
