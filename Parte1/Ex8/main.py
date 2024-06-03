
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


def main():

    # ------------------------------------------------------
    # Initialization
    # ------------------------------------------------------
    filename = '/home/mike/sharedVBWindows/MVA_6-24/MVA_24-25/Parte1/imagens/grey_lake.jpg'
    # filename = '/home/mike/sharedVBWindows/MVA_6-24/MVA_24-25/Parte1/imagens/chess.png'

    if not os.path.isfile(filename):
        print('filename ' + filename + ' does not exist')

    # Load the image
    image = cv2.imread(filename,  cv2.IMREAD_GRAYSCALE)

    # ------------------------------------------------------
    # Execution
    # ------------------------------------------------------

    # Resize of image
    image_resized = cv2.resize(image, (400, 200), interpolation=cv2.INTER_LINEAR)

    # create mosaic
    h, w = image_resized.shape
    mosaic = np.zeros((h*2, w*2), dtype=np.uint8)
    print('mosaic shape = ' + str(mosaic.shape))

    print(image_resized.shape)

    mosaic[0:200, 0:400] = image_resized
    mosaic[0:200, 400:800] = image_resized

    mosaic[200:400, 0:400] = image_resized
    mosaic[200:400, 400:800] = image_resized

    cv2.imshow('image', image)
    cv2.imshow('image_resized', image_resized)
    cv2.imshow('mosaic', mosaic)

    # Wait for the user to press a key
    cv2.waitKey(0)

    # ------------------------------------------------------
    # Termination
    # ------------------------------------------------------

    # Close all windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
