import time

try:
    while True:
        print("走行中...")
        time.sleep(1)
except KeyboardInterrupt:
    print("Ctrl+C が押されました")
finally:
    print("モータを停止します")
