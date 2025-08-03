from load_image import ft_load
from matplotlib import pyplot as plt
import numpy as np


def crop_image(image: np.array, x_start: int,
               y_start: int, x_size: int, y_size: int):
    """crop a subsection of an image array starting from
    (x_start, y_start) with width (x_size), height (y_size)"""

    (n, m, _) = image.shape
    if (x_start < 0 or x_size <= 0 or y_size <= 0 or y_start < 0):
        raise ValueError("coordinates and sizes must be positive int")

    if (x_start + x_size > m or y_start + y_size > n):
        raise ValueError("Crop area exceeds image bounds")

    croped_image = image[y_start: y_start + y_size,
                         x_start: x_start + x_size, :1]
    return croped_image


def main():
    """load the image "animal.jpeg", print some information
    about it and display it after "zooming"."""
    x_size = 400
    y_size = 400
    x_start = 450
    y_start = 100

    try:
        image = ft_load("animal.jpeg")
        cropped = crop_image(image, x_start, y_start, x_size, y_size)

        print(f"The shape of image is: {image.shape}")
        print(image)
        print(f"New shape after slicing: {cropped.shape}", end='')
        print(f" or {cropped.shape[0:2]}")
        print(cropped)

        plt.imshow(cropped, cmap="gray")
        plt.show()

    except Exception as e:
        print(f"{type(e).__name__}: {e}")

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
