def is_even(n):
    if isinstance(n, (int, float)):
        if isinstance(n, int):
            return n%2 == 0
        else:
            return n.is_integer()
    else:
        return False