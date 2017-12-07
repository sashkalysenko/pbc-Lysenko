import argparse


def pairs(*args):
    """returns unique pairs of numbers with sum which equals to 10"""

    unique_pairs = set()

    for i in range(len(args)):
        for m in args[i+1:]:
            if args[i] + m == 10:
                unique_pairs.add(tuple(sorted([args[i], m])))

    return list(unique_pairs)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Returns unique pairs of numbers with sum which equals to 10")
    parser.add_argument('-n', '--numbers', nargs="+", type=int, help='List of numbers')
    args = parser.parse_args()

    print(pairs(*args.numbers))
