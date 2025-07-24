
def ft_tqdm(lst: range) -> None:
    """def ft_tqdm(lst: range) -> None\n
    function that iterates over a range and displays a progress bar
    and the current iteration count over the total number of elements.
    """

    total = len(lst)
    bar_width = 70

    for i, elem in enumerate(lst):
        percent = int((i + 1) / total * 100)
        filled = int((i + 1) / total * bar_width)
        bar = '=' * (filled - 1) + '>'
        print(f"\r{percent:3d}%|[{bar:<{bar_width}}]| {i + 1}/{total}", end='')
        yield elem
