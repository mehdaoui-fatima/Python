import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    """loads an image, prints its format and pixels content in RGB format."""
    try:
        image = Image.open(path)
        assert image.format in ['JPEG', 'JPG'], "Only JPEG/JPG are supported"
        np_image = np.array(image)
        return np_image

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
