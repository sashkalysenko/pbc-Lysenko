def print_pairs(*args):
    """returns unique pairs of numbers with sum which equals to 10"""

    pairs = []

    for i in range(len(args)):
        for m in args[i+1:]:
            if args[i] + m == 10:
                pairs.append(tuple(sorted([args[i], m])))

    for pair in set(pairs):
        print("{0}+{1}".format(pair[0], pair[1]))
