# 練習問題：誤りを探して直すプログラム（このままでは正しく動かない）
import random

hands = ["グー", "チョキ", "パー"]
judge = ["あいこ", "負け", "勝ち"]

player = input("0:グー、1:チョキ、2:パー >>> ")
if player == 0 and player == 1 and player == 2:
    prin("あなた: " + hands[player])
    computer = random.randint(0, 3)
    print("コンピュータ: " + hands[computer])
    decision = (player - computer + 3) % 3
    print("結果は「" + judge[dceision] + "」です")
