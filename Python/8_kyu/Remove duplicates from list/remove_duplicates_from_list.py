def distinct(seq):
    seen = set()
    result = []
    for elem in seq:
        if elem not in seen:
            seen.add(elem)
            result.append(elem)
    return result
