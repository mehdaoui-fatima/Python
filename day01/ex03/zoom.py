from  load_image import ft_load
from matplotlib import pyplot as plt
import numpy as np


# positive values
# raneg in image dimension
# ceck for other errors to handel 

def crop_image(image: np.array, x_start: int, y_start: int, x_size: int, y_size: int, depth: int):

    try:
        if (x_start < 0 or x_size < 0 or y_size < 0 or y_start < 0):
            raise TypeError("All crop dimensions must be positive")
        croped_image = image[y_start: y_start + y_size, x_start: x_start + x_size, :1]
        return croped_image
    
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        exit()


def main():

    x_size = 400
    y_size = 7400
    x_start = 7450
    y_start = 16645645645650

    try:
        image = ft_load("animal.jpeg")
        croped_image = crop_image(image, x_start, y_start, x_size, y_size, depth=1)
        
        print(f"The shape of image is: {image.shape}")
        print(image)
        print(f"New shape after slicing: {croped_image.shape} or {croped_image.shape[:2]}")
        print(croped_image)

        plt.imshow(croped_image, cmap="gray")
        plt.show()
    
    except Exception as e:
        print(f"{type(e).__name__}: {e}")

    except KeyboardInterrupt as e:
        pass

if __name__ == "__main__":
    main()
