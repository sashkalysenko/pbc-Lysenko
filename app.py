import argparse
from pbc.tools.fibonacci import fibonacci
from pbc.tools.numbers import pairs

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Runs one of the applications: fibonacci or unique_pairs")
    parser.add_argument('-fib', '--fibonacci', type=int, help='Runs fibonacci app. Need to set number of sequence')
    parser.add_argument('-up', '--unique_pairs', nargs="+", type=int, help='Runs unique_pairs app. List of numbers '
                                                                           'is required')
    args = parser.parse_args()

    if args.fibonacci:
        print(fibonacci(args.fibonacci))
    if args.unique_pairs:
        for item in pairs(*args.unique_pairs):
            print("{0}+{1}".format(item[0], item[1]))
    if not(args.fibonacci and args.unique_pairs):
        raise Exception("At least one arguments is expected. See help")
