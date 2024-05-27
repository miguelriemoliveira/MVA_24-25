
import cv2
import os
import numpy as np


def main():

    filename = '/home/mike/sharedVBWindows/MicroCredencialVisãoArtificial/MVA_24-25/Parte1/imagens/grey_lake.jpg'

    if not os.path.isfile(filename):
        print('filename ' + filename + ' does not exist')

    # Load the image
    image = cv2.imread(filename,  cv2.IMREAD_GRAYSCALE)

    print(type(image))
    print(image.shape)

    # reduce depth
    level = 64
    # levels = 63,32,16 8

    factor = 256/level
    image_64 = (np.floor(image.astype(float) / factor) * factor).astype(np.uint8)

    # Display the image
    cv2.imshow('Image', image)

    cv2.imshow('Image64', image_64)

    # Wait for the user to press a key
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
