import sys

def main():
    """This program counts the number of upper case letters, lower case letters,
    punctuation marks, spaces, and digits in a given text."""

    argv_len = len(sys.argv)

    counts = {
        "upper": 0,
        "lower": 0,
        "punctuation": 0,
        "spaces": 0,
        "digits": 0,
    }

    try:
        if argv_len > 2:
            raise AssertionError("more than one argument is provided")
        elif argv_len < 2:
            print("What is the text to count?")
            text = sys.stdin.read()
        else:
            text = sys.argv[1]

        
        for letter in text:
            if (letter.isupper()):
                counts["upper"] += 1
            elif (letter.islower()):
                counts["lower"] += 1
            elif (letter in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"):
                counts["punctuation"] += 1
            elif (letter.isspace() or letter == '\n'):
                counts["spaces"] += 1
            elif (letter.isdigit()):
                counts["digits"] += 1
        
        print(f"The text contains {len(text)} characters:")
        print(f"{counts['upper']} upper letters")
        print(f"{counts['lower']} lower letters")
        print(f"{counts['punctuation']} punctuation marks")
        print(f"{counts['spaces']} spaces")
        print(f"{counts['digits']} digits")

    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")

    except:
        pass

if __name__ == "__main__":
    main()