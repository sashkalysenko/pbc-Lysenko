def print_pairs(numbers):
    """returns unique pairs of numbers with sum which equals to 10"""

    pairs = []

    for i in range(len(numbers)):
        for m in numbers[i+1:]:
            if numbers[i] + m == 10:
                pairs.append(tuple(sorted([numbers[i], m])))

    return set(pairs):
