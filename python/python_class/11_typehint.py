import math


def wheel_speed(rps: float, radius: float = 0.033) -> float:
    return 2 * math.pi * radius * rps


def valid_average(distances: list[float]) -> float | None:
    valid = [d for d in distances if d >= 0]
    if len(valid) == 0:
        return None
    return sum(valid) / len(valid)


print(wheel_speed(2.0))
print(valid_average([1.2, -1.0, 0.8]))
