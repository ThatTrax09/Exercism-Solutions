def sum_of_multiples(limit, multiples):
    multiple_set = set()
    for number in multiples:
        if number == 0:
            continue
        multiple_set |= {m for m in range(number, limit, number)}
    return sum(list(multiple_set))
