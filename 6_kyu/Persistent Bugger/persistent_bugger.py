def persistence(n: int) -> int:
    def multiply_digits(num: int) -> int:
        product = 1
        for digit in str(num):
            product *= int(digit)
        return product

    count = 0
    while n > 9:
        n = multiply_digits(n)
        count += 1
    return count



