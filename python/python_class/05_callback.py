import time


def run_timer(period, count, callback):
    # period 秒ごとに、callback を count 回呼び出す
    for i in range(count):
        time.sleep(period)
        callback(i)


def say_hello(i):
    print(f"{i} 回目: こんにちは")


def check_battery(i):
    print(f"{i} 回目: バッテリを確認しました")


run_timer(0.5, 3, say_hello)       # ( ) を付けずに関数を渡す
run_timer(0.5, 2, check_battery)
