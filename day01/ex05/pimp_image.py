import numpy as np

# doc string anad type return
#  norm 
#  tests and errors handling anad exceptions

def ft_invert(array):
   """Inverts the color of the image received."""
   Imax = 255
   invert = Imax - array 
   return invert 

# r g b  255 255 255
def ft_red(array):
   array[:,:,1] = 0
   array[:,:,2] = 0
   return array 

def ft_green(array):
   array[:,:,0] = 0
   array[:,:,2] = 0
   return array



def ft_blue(array):
   array[:,:,0] = 0
   array[:,:,1] = 0
   return array



def ft_grey(array):
    R = array[:, :, 0]
    G = array[:, :, 1]
    B = array[:, :, 2]

    # Compute weighted sum for grayscale (luminosity method)
    gray_values = R * 0.299 + G * 0.587 + B * 0.114

    # Create a copy of the original array to preserve shape and dtype
    gray_image = array.copy()

    # Assign grayscale values to each channel
    for channel in range(3):
        gray_image[:, :, channel] = gray_values

    # Convert back to original dtype (usually uint8)
    return gray_image