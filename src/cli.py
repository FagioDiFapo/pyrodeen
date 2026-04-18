import argparse

def parse():
    parser = argparse.ArgumentParser(description="PyRoDeEn CLI")
    parser.add_argument('-t1', '--test_grid', help='Test grid object', action='store_true')

    return parser.parse_args()

def main():
    args = parse()

    if args.test_grid:
        from grid import test_grid
        test_grid()

if __name__ == "__main__":
    main()