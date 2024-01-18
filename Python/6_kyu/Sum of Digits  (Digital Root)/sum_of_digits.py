def digital_root(n: int) -> int:
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n