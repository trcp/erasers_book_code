money = 4000
book = 980
chips = 250
ice = 150
book_tax = 0.10
food_tax = 0.08

total = book * 2 * (1 + book_tax) + (chips + ice) * (1 + food_tax)
print(round(money - total))   # 1412
