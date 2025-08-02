import numpy as np
from load_image import ft_load
from matplotlib import pyplot as plt


# plt.imshow(array_gray, cmap='gray')
# plt.axis('off')

def rotate(image):
    rows = len(image)
    columns = len(image[0])

    # init 
    transposed = [[0 for _ in range(columns)] for _ in range(rows)]
    # transpose
    for i in range(rows):
        for j in range(columns):
            transposed[i][j] = image[j][i]

    return np.asarray(transposed)

def main():
    x_size = 400
    y_size = 400
    x_start = 450
    y_start = 100

    image = ft_load("animal.jpeg")
    croped_image = image[y_start: y_start + y_size, x_start: x_start + x_size, 1]
    rotated_image = rotate(croped_image)

    plt.imshow(rotated_image, cmap="gray")
    plt.show()

if __name__ == '__main__':
    main()

