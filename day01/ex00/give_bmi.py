import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate the BMI for corresponding elements in height and weight lists.

    Parameters:
        height (list[int | float]): List of heights in meters.
        weight (list[int | float]): List of weights in kilograms.

    Returns:
        list[float]: List of calculated BMI values.
    """
    try:
        height = np.asarray(height)
        weight = np.asarray(weight)

        if weight.shape != height.shape:
            raise ValueError("height and weight must have same size")

        if weight.dtype not in [np.dtype(int), np.dtype(float)]:
            raise ValueError("weight list elements must be float or int")

        if height.dtype not in [np.dtype(int), np.dtype(float)]:
            raise ValueError("height list elements must be float or int")

        if np.any(height == 0):
            raise ValueError("height list elements must be > 0")

        return (weight / (height * height)).tolist()

    except ValueError as e:
        print(f"{type(e).__name__}: {e}")
        return []


def apply_limit(bmi: list[int | float],
                limit: int) -> list[bool]:
    """
    Compare each value in a list to a specified limit.

    Parameters:
        bmi (list[int | float]): A list of integers or floats representing BMI.
        limit (int): The value to compare against.

    Returns:
        list[bool]: A list of booleans where each element is True if the
        BMI value is greater than the limit, and False otherwise.
    """
    return [nb > limit for nb in bmi]
