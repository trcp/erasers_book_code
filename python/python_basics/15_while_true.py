while True:
    num = int(input("1〜100 の値を入力してください=> "))
    if 1 <= num <= 100:
        break
    print("範囲外の値です")
print(f"入力された値は {num} です")
