def clamp(value, low, high):
    """value を low 以上 high 以下の範囲に収める"""
    if value < low:
        return low
    if value > high:
        return high
    return value


if __name__ == "__main__":
    # このファイルを直接実行したときだけ動く（動作確認用）
    print(clamp(1.5, -1.0, 1.0))
