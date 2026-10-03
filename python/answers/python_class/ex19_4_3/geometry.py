import math


def distance(x1, y1, x2, y2):
    """2 点間の距離を返す"""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def normalize_angle(deg):
    """角度を -180 以上 180 未満に正規化する"""
    return (deg + 180) % 360 - 180
