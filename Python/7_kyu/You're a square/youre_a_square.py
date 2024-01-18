from math import sqrt


def is_square(n: int) -> bool:
    return sqrt(n).is_integer() if n >= 0 else False
