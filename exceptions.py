"""A module for demonstrating exceptions."""


def convert_int(s):
    """Convert to an integer."""
    try:
        x = int(s)
        print("Conversion succeeded! x = ", x)
    except ValueError:
        print("Conversion failed!")
        x = -1
    return x


def main():
    convert_int("1234")
    convert_int("not a number")
    convert_int("4321")


if __name__ == "__main__":
    main()
