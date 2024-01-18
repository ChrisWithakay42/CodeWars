def last_man_standing(n):
    if n == 1:
        return 1

    # Initialize a list of numbers from 1 to n
    numbers = list(range(1, n + 1))
    is_left = True  # Flag to determine whether to remove from the left or right

    while len(numbers) > 1:
        if is_left:
            # Remove every other number from the list by slicing
            numbers = numbers[1::2]
        else:
            # Remove every other number from the list by slicing in reverse
            numbers = numbers[-2::-2][::-1]

        is_left = not is_left  # Switch the direction for the next iteration

    return numbers[0]


