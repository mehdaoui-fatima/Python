import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate the BMI for corresponding elements in height and weight lists.
    """

    try:
        print(len(height))
        if (len(height) != len(weight) or len(height) == 0):
            raise ValueError("""lists must be non-empty
                             and have the same length""")

        # All Returns true if all of the items are True
        # (or if the iterable is empty)
        if not all([isinstance(item, (int, float)) for item in height]):
            raise TypeError("All height elements must be int or float")

        if not all([isinstance(item, (int, float)) for item in weight]):
            raise TypeError("All weight elements must be int or float")

        weight = np.asarray(weight)
        height = np.asarray(height)

        if np.any(height <= 0):
            raise ValueError("height list elements must be > 0")

        bmi_vaues = weight / (height * height)

        return bmi_vaues.tolist()

    except (ValueError, TypeError) as e:
        print(f"{type(e).__name__}: {e}")
        return []


def apply_limit(bmi: list[int | float],
                limit: int) -> list[bool]:
    """
    Compare each value in a list to a specified limit.
    to retrun a list of booleans where each element is True if the
        BMI value is greater than the limit, and False otherwise.
    """
    return [nb > limit for nb in bmi]
