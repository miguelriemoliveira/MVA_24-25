
import cv2
import os
import numpy as np
import random


def main():

    filename = '/home/mike/sharedVBWindows/MicroCredencialVisãoArtificial/MVA_24-25/Parte1/imagens/chessboard.jpg'

    if not os.path.isfile(filename):
        print('filename ' + filename + ' does not exist')

    # Load the image
    image = cv2.imread(filename,  cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Original image', image)

    h = image.shape[0]
    w = image.shape[1]

    # TODO Percorra todos os pixeis da imagem imagens/chessboard.jpg e, para cada um,
    # a) altere o seu valor para metade
    # b) com uma probabilidade de 50%.

    for row in range(0, h):  # percorre todas as linhas
        for col in range(0, w):  # percorre todas as colunas
            value = random.random()

            if row > h/2:
                if value > 0.9:
                    image[row, col] = image[row, col] / 2
            else:
                if value > 0.1:
                    image[row, col] = image[row, col] / 2

            # Display the image

    cv2.imshow('Image', image)

    # Wait for the user to press a key
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
