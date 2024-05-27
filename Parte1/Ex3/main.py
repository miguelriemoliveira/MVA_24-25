
import cv2
import os
import numpy as np
import random


def main():

    # Load the image
    # TODO create an image 200x300 black
    # image = ...

    cv2.imshow('Original image', image)

    # h = image.shape[0]
    # w = image.shape[1]

    # TODO Colocar um rectangulo branco

    # TODO Colocar um rectangulo cinzento

    # for row in range(0, h):  # percorre todas as linhas
    #     for col in range(0, w):  # percorre todas as colunas
    #         value = random.random()

    #         if row > h/2:
    #             if value > 0.9:
    #                 image[row, col] = image[row, col] / 2
    #         else:
    #             if value > 0.1:
    #                 image[row, col] = image[row, col] / 2

    #         # Display the image

    cv2.imshow('Image', image)

    # Wait for the user to press a key
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
