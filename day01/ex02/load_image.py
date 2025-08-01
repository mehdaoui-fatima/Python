import numpy as np
from PIL import Image

def ft_load(path: str) -> np.array:

    try:
        assert len(path) > 0, 'Invalid path file'
        image = Image.open(path)
        assert image.format in ['JPEG', 'JPG'], "Invalid file format"
        np_image = np.array(image)
      
        return np_image

    except Exception as e:
        print(f"{type(e).__name__}: {e}")

