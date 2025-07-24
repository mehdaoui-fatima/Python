import sys


# if the function def doest contain return statement,
# the default return is None.
def parity(x: int) -> str:
    if (int(x) % 2 == 0):
        return "I'm Even."
    else:
        return "I'm Odd."


try:
    if len(sys.argv) == 1:
        sys.exit()
    # assert condition, error_message
    assert len(sys.argv) == 2, "more than one argument is provided"
    int(sys.argv[1])
    print(parity(sys.argv[1]))

except ValueError:
    print(f'{AssertionError.__name__}: argument is not an integer')

except Exception as e:
    print(f'{AssertionError.__name__}: {e}')
