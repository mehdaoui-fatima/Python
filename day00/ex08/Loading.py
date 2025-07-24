


# TODO
# doc string
# norm and clear code from tests files
# tests with file correction
#  understanding well  
# change input to stdin.read from sys in ex05

def ft_tqdm(lst: range) -> None:
    total = len(lst)
    bar_width = 70

    for i, elem in enumerate(lst):
        percent = int((i + 1) / total * 100)
        filled = int((i + 1) / total * bar_width)
        bar = '=' * (filled - 1) + '>'
       

        print(f"{percent:3d}%|[{bar:<{bar_width}}]| {i + 1}/{total}", end='\r')
        yield elem