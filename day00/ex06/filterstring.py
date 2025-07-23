from sys import argv
from ft_filter import ft_filter


# doc string 
# norm 
def main():
    """ doc string needed """

    argv_len = len(argv)
    try:

        # if argv_len != 3:
        #     raise AssertionError("the arguments are bad")
        s = argv[1]
        n = argv[2]
        
        assert isinstance(s, str), "the arguments are bad"
        assert isinstance(n, int), "the arguments are bad"

        ft_words = ft_filter(lambda x: len(x) > int(n), s.split())
        print(ft_words)

    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")


    



if __name__ == "__main__":
    main()


