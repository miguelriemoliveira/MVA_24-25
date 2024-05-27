
import cv2
import os
import numpy as np
import random


def main():

    # Load the image
    # TODO create an image 200x300 black
    image = np.zeros((200, 300)).astype(np.uint8)
    # image = np.zeros((200, 300), dtype=np.uint8)

    cv2.imshow('Original image', image)

    h = image.shape[0]
    w = image.shape[1]

    x0 = w/2
    y0 = h/2
    r = 45

    for y in range(0, h):  # percorre todas as linhas
        for x in range(0, w):  # percorre todas as colunas

            if (x-x0)**2 + (y-y0)**2 < r**2:  # estamos dentro da circ
                image[y, x] = 255

    cv2.imshow('Image', image)

    # Wait for the user to press a key
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
