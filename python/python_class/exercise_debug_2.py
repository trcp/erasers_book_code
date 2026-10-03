# 練習問題：誤りを探して直すプログラム（このままでは正しく動かない）
num = input("数値を入力=> ")

for i in range(num):
    if i % 5 == 2 or 3:
        print("i")
