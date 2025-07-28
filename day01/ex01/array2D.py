import numpy as np

# __doc__
# norme
# test inhomogeneous shape

def handelErros(family: list):
    if not isinstance(family, list):
        raise TypeError("First argument must be a list")

    if not all(isinstance(row, list) for row in family):
        raise TypeError("Each element of the main list must be a list")

    expected_len = len(family[0])
    if not all(len(row) == expected_len for row in family):
        raise ValueError("All inner lists must have the same size")



def slice_me(family: list, start: int, end: int) -> list:
    try:
        handelErros(family)
    
        np_list = np.asarray(family)
        np_list_shape = np_list.shape
        print(f"My shape is : {np_list_shape}")

        np_list = np_list[start: end]
        np_list_shape = np_list.shape
        print(f"My new shape is : {np_list_shape}")

        return np_list.tolist()

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return list()

