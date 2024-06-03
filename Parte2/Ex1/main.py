
import random
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


def main():

    # ------------------------------------------------------
    # Initialization
    # ------------------------------------------------------
    filename = '/home/mike/sharedVBWindows/MVA_6-24/MVA_24-25/Parte2/imagens/parrot.png'
    if not os.path.isfile(filename):
        print('filename ' + filename + ' does not exist')

    # Load the image
    image = cv2.imread(filename,  cv2.IMREAD_GRAYSCALE)
    h, w = image.shape

    # ------------------------------------------------------
    # Execution
    # ------------------------------------------------------
    # Add noise

    flip_flop = False  # init flip_flop
    for x in range(0, w):
        for y in range(0, h):
            if random.random() > (1-0.05):  # add noise

                if flip_flop:  # paint white (salt)
                    image[y, x] = 255
                else:  # paint black (pepper)
                    image[y, x] = 0

                flip_flop = not flip_flop  # invert flip flop

    # ------------------------------------------------------
    # Visualization
    # ------------------------------------------------------
    window_name = 'Image'
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    cv2.resizeWindow(window_name, w*4, h*4)
    cv2.imshow(window_name, image)

    # Wait for the user to press a key
    cv2.waitKey(0)

    # ------------------------------------------------------
    # Termination
    # ------------------------------------------------------

    # Close all windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
