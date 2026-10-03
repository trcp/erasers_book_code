# 練習問題 18.5 (1)
total = 0
for i in range(1, 31):
    total += i
print(total)   # 465

# 練習問題 18.5 (2)
nums = [1, 62, 3, 6743, 51, 6783, 42, 4671, 5, 236]
for n in nums:
    if n >= 1000:
        continue
    print(n)

# 練習問題 18.5 (3)
n = int(input("数> "))
for i in range(1, n + 1):
    print(f"{i}:" + "■" * i)

# 練習問題 18.5 (4)
count = 0
total = 0
while True:
    data = float(input("データ入力（負の数で終了）> "))
    if data < 0:
        break
    count += 1
    total += data
if count > 0:
    print(f"個数: {count} 合計: {total} 平均: {total / count}")
