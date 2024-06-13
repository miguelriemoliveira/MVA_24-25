
from copy import deepcopy
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

# Global variables
image = None
image_flodded = None
mask_flooded = None

# functions


def mouseCallback(event, x, y, flags, param):
    global image, image_flodded, mask_flooded

    if event == cv2.EVENT_LBUTTONDBLCLK:
        print('x= ' + str(x) + ' y=' + str(y))

        # prepare flood fill parameters
        h, w = image.shape
        image_to_flood = image
        mask_to_flood = np.zeros((h+2, w+2), dtype=np.uint8)
        mask_to_flood[int(h/2), :] = 255
        seed = (x, y)
        new_val = 128
        low = 10
        up = 10
        flags = 4 | (new_val << 8) | cv2.FLOODFILL_MASK_ONLY

        # run the flood fill
        _, image_flodded, mask_flooded, _ = cv2.floodFill(image_to_flood, mask_to_flood,
                                                          seed, new_val, low, up, flags)


def main():
    global image, image_flodded, mask_flooded

    # --------------------------
    # Initialization
    # --------------------------
    filename = '/home/mike/sharedVBWindows/MVA_6-24/MVA_24-25/Parte3/imagens/lena.jpg'
    if not os.path.isfile(filename):
        print('filename ' + filename + ' does not exist')

    # Load the image
    image = cv2.imread(filename,  cv2.IMREAD_GRAYSCALE)

    cv2.namedWindow('Image')
    cv2.setMouseCallback('Image', mouseCallback)
    cv2.imshow('Image', image)

    # --------------------------
    # Execution
    # --------------------------
    while True:

        if image_flodded is not None:
            cv2.imshow('image_flooded', image_flodded)

        if mask_flooded is not None:
            cv2.imshow('mask_flooded', mask_flooded)
        cv2.waitKey(50)

    # Close all windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
