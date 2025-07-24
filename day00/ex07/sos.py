from sys import argv


def main():
    """the program takes a string as an argument and encodes it into Morse Code."""
    
    argv_len = len(argv)
    NESTED_MORSE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}

    try:
        if argv_len != 2:
            raise AssertionError("the arguments are bad")
        if not argv[1].isalnum():
            raise AssertionError("the arguments are bad")
              
        encoded = ''
        for it in argv[1]:
            encoded = encoded + NESTED_MORSE[it.upper()] + ''

        encoded.strip() 
        print(f"{encoded}")
    

    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")


if __name__ == "__main__":
    main()