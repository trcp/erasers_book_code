# 練習問題 18.6 (1)
def motto():
    print("完璧を")
    print("目指すよりも")
    print("まずは")
    print("終わらせろ")


motto()
motto()
motto()


# 練習問題 18.6 (2)
def even_or_odd(num):
    if num % 2 == 0:
        print("偶数")
    else:
        print("奇数")


even_or_odd(5)
even_or_odd(20)
even_or_odd(1)


# 練習問題 18.6 (3)
def maximum(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest


print(maximum(40, 23, 60))   # 60


# 練習問題 18.6 (4)
def find_max_min(values):
    return max(values), min(values)


largest, smallest = find_max_min([3, 62, 4, 56, 346, 8, 2, 893, 52, 46])
print(largest, smallest)   # 893 2


# 練習問題 18.6 (5)
def valid_average(distances):
    valid = []
    for d in distances:
        if d >= 0:
            valid.append(d)
    if len(valid) == 0:
        return None
    return sum(valid) / len(valid)


print(valid_average([1.2, -1.0, 0.8]))   # 1.0
print(valid_average([-1.0, -1.0]))       # None
