import argparse
from importlib.metadata import version


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", help="Show version", action="store_true")
    args = parser.parse_args()

    if args.version:
        ver = version("lliv")
        print(f"lliv - {ver}")


if __name__ == "__main__":
    main()
