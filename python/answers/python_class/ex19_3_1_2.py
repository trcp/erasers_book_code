# 練習問題 19.3 (1)
def apply_all(values, func):
    results = []
    for v in values:
        results.append(func(v))
    return results


def to_cm(m):
    return m * 100


print(apply_all([1.0, 2.5, 4.0], to_cm))   # [100.0, 250.0, 400.0]


# 練習問題 19.3 (2)
def watch(distances, on_obstacle):
    for d in distances:
        if d < 0.3:
            on_obstacle(d)


def warn(d):
    print(f"障害物を検出: {d} m")


watch([1.2, 0.25, 0.8, 0.1], warn)
