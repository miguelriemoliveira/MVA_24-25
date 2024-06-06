
from copy import deepcopy
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


def main():

    # --------------------------
    # Initialization
    # --------------------------
    filename = '/home/mike/sharedVBWindows/MVA_6-24/MVA_24-25/Parte3/imagens/wdg2.bmp'
    if not os.path.isfile(filename):
        print('filename ' + filename + ' does not exist')

    # Load the image
    image = cv2.imread(filename,  cv2.IMREAD_GRAYSCALE)
    h, w = image.shape

    # --------------------------
    # Execution
    # --------------------------

    # step 1 - threshold the image with value 120
    bw = image > 120
    print(bw.dtype)

    # step 2 - invert the image
    bw2 = np.logical_not(bw)

    # step 3 - dilation
    se = np.ones(11, dtype=np.uint8)*255

    cv2.imshow('bw2', bw2.astype(np.uint8)*255)

    bw2_dilated = deepcopy(bw2).astype(np.uint8)*255  # ensure that a real copy is made

    for i in range(10):
        bw2_dilated = cv2.dilate(bw2_dilated, se, iterations=1)

        # cv2.imshow('bw2_dilated', bw2_dilated)
        cv2.destroyAllWindows()
        cv2.imshow('bw2_dilated i=' + str(i), bw2_dilated)
        # Wait for the user to press a key
        cv2.waitKey(0)

    # --------------------------
    # Visualization
    # --------------------------

    # Display the image
    # cv2.imshow('Image', image)
    # cv2.imshow('bw', bw.astype(np.uint8)*255)

    # Close all windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
