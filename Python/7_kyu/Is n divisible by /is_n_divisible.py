def is_divisible(n: int, *args:int) -> bool:
    # if not args:
    #     return True
    #
    # for num in args:
    #     if n % num != 0:
    #         return False
    # return True
    return all(not n % num for num in args)