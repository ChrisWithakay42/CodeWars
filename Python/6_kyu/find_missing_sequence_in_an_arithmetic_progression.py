def find_missing(sequence: list) -> int:
    common_diff = (sequence[-1] - sequence[0]) // len(sequence)

    for idx, value in enumerate(sequence[1:], start=1):
        if (value - sequence[idx - 1]) != common_diff:
            missing_term = sequence[idx - 1] - common_diff
            return missing_term
    return 0
