def parts_sums(ls):
    total_sum = sum(ls)
    result = [total_sum]

    for num in ls:
        total_sum -= num
        result.append(total_sum)

    return result
