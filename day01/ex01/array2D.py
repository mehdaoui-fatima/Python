import numpy as np


def handelErrors(family: list):
    """ Validate that the input is a non-empty
        2D list with equal-length rows."""
    if not isinstance(family, list):
        raise TypeError("First argument must be a list")

    if not all(isinstance(row, list) for row in family):
        raise TypeError("Each element of the main list must be a list")

    columns = len(family[0])
    if not all(len(row) == columns for row in family):
        raise ValueError("All inner lists must have the same size")


# slice: array[row_start:row_stop:row_step, col_start:col_stop:col_step]
def slice_me(family: list, start: int, end: int) -> list:
    """slice a given array using start and end positions."""
    try:
        handelErrors(family)
        np_list = np.asarray(family)
        n, m = np_list.shape
        print(f"My shape is : {(n,m)}")

        np_slice = np_list[start:end]
        print(f"My new shape is : {np_slice.shape}")

        return np_slice.tolist()

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return list()
