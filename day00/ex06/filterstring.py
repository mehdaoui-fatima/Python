from sys import argv
from ft_filter import ft_filter


def main():
    """a program that accepts two arguments: a string(S),
    and an integer(N).\n
    The program output a list of words from S
    that have a length greater than N."""

    argv_len = len(argv)
    try:
        if argv_len != 3:
            raise AssertionError("the arguments are bad")
        s = argv[1]
        n = int(argv[2])

        assert isinstance(s, str), "the arguments are bad"
        assert isinstance(n, int), "the arguments are bad"

        ft_words = ft_filter(lambda x: len(x) > int(n), s.split())
        print(ft_words)

    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")

    except ValueError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
