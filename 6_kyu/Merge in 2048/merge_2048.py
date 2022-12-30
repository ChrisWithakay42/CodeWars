def merge(row: list[int]) -> list[int]:
    non_zero_tiles = [value for value in row if value != 0]

    merged = [0] * (len(row) - len(non_zero_tiles))

    i = 0
    while i < len(non_zero_tiles):
        if i+1 < len(non_zero_tiles) and non_zero_tiles[i] == non_zero_tiles[i+1]:
            merged.append(non_zero_tiles[i] * 2)
            i += 2
        else:
            merged.append(non_zero_tiles[i])
            i += 1

    return merged

