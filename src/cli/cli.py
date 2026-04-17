import argparse

def parse():
    parser = argparse.ArgumentParser(description="PyRoDeEn CLI")
    parser.add_argument("test_grid", help="Your name")

    return parser.parse_args()

def main():
    args = parse()

    if args.test_grid:
        from grid.grid import test_grid
        test_grid()


if __name__ == "__main__":
    main()