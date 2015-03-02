"""A module for demonstrating exceptions."""


def convert(s):
    """Convert to an integer."""
    try:
        x = int(s)
        print("Conversion succeeded! x = ", x)
    except ValueError:
        print("Conversion failed!")
        x = -1
    return x


def main():
    convert("1234")


if __name__ == "__main__":
    main()
