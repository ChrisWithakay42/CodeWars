def get_last_digit(index):
    if index <= 1:
        return index

    a, b = 0, 1
    for _ in range(2, index + 1):
        a, b = b, (a + b) % 10
    return b