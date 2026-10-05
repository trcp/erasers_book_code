def price_with_tax(price, tax_rate=0.1):
    return round(price * (1 + tax_rate))


def min_max(values):
    return min(values), max(values)


print(price_with_tax(980))                  # 税率 10% で計算
print(price_with_tax(250, tax_rate=0.08))   # 税率 8% で計算
low, high = min_max([1.2, 0.8, 0.5, 1.5])
print(low, high)
