import numpy as np
from PIL import Image

def ft_load(path: str) -> np.array:

    try:
        assert len(path) > 0, 'Invalid path file'
        image = Image.open(path)
        assert image.format in ['JPEG', 'JPG'], "Invalid file format"
        np_image = np.array(image)

        print(f"The shape of image is: {np_image.shape}")
        return np_image
  
    except  AssertionError as e:
        print(f"{type(e).__name__}: {e}")

    except Exception as e:
        print(f"{type(e).__name__}: {e}")

    
