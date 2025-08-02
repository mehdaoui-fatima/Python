from load_image import ft_load 
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
from matplotlib import pyplot as plt


image = ft_load("landscape.jpeg")

# invert = ft_invert(image)
# print(ft_invert.__doc__)
# plt.imshow(invert)
# plt.show()

# red = ft_red(image)
# print(ft_red.__doc__)
# plt.imshow(image)
# plt.show()

# green = ft_green(image)
# print(ft_green.__doc__)
# plt.imshow(image)
# plt.show()

# blue = ft_blue(image)
# print(ft_blue.__doc__)
# plt.imshow(image)
# plt.show()

grey = ft_grey(image)
print(ft_grey.__doc__)
plt.imshow(grey)
plt.show()


# plt.imshow(image[:, :, 1], cmap='grey')
# plt.show()
