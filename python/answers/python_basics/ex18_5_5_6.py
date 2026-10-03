import random

# 練習問題 18.5 (5)
answer = random.randint(1, 30)
for i in range(5):
    guess = int(input("値を入力してください=> "))
    if guess == answer:
        print("正解です！")
        break
    elif guess < answer:
        print("残念！それよりも大きいです！")
    else:
        print("残念！それよりも小さいです！")
print(f"正解は {answer} でした。")

# 練習問題 18.5 (6)
hands = ["グー", "チョキ", "パー"]
results = ["あいこ", "負け", "勝ち"]
mine = int(input("あなたの手は？（0:グー, 1:チョキ, 2:パー）=> "))
computer = random.randint(0, 2)
print(f"あなた: {hands[mine]}  コンピュータ: {hands[computer]}")
print(results[(mine - computer + 3) % 3])
