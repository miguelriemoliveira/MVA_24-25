
import random
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


def main():

    # ------------------------------------------------------

    # Initialization

    # ------------------------------------------------------

    # TODO Create a black image with 400x600
    """
    filename = '/home/mike/sharedVBWindows/MVA_6-24/MVA_24-25/Parte2/imagens/parrot.png'
    if not os.path.isfile(filename):
        print('filename ' + filename + ' does not exist')
    # Load the image
    image = cv2.imread(filename,  cv2.IMREAD_GRAYSCALE)
    """

    # criar imagem
    image = np.zeros((500, 500)).astype(np.uint8)+90
    h, w = image.shape

    # ------------------------------------------------------
    # Execution
    # ------------------------------------------------------
    flip_flop = False  # init flip_flop

    for x in range(0, w):
        for y in range(0, h):
            if random.random() > (1-0.2):  # add noise
                if flip_flop:  # paint white (salt)
                    image[y, x] = 255
                else:  # paint black (pepper)
                    image[y, x] = 0
                flip_flop = not flip_flop  # invert flip flop

    # ------------------------------------------------------
    # Visualization
    # ------------------------------------------------------

    window_name = 'Image'
    # cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    # cv2.resizeWindow(window_name, w*4, h*4)
    cv2.imshow(window_name, image)

    # filtro de media
    image2 = cv2.blur(image, (3, 3))
    window_name2 = 'media'
    cv2.imshow(window_name2, image2)

    # filtro mao
    f = np.ones((3, 3), dtype=float)*(1/9)  # equivalente a filtro de media
    print(f)

    results = (image*0).astype(float)
    for x in range(1, w-1):
        for y in range(1, h-1):
            subimage = (image[y-1:y+2, x-1:x+2]).astype(float)
            subres = np.multiply(subimage, f)
            som_subres = np.sum(subres)
            results[y, x] = som_subres

    results = results.astype(np.uint8)

    window_name5 = 'calculo_mao'
    cv2.imshow(window_name5, results)

    # Wait for the user to press a key
    cv2.waitKey(0)

    # ------------------------------------------------------
    # Termination
    # ------------------------------------------------------

    # Close all windows
    cv2.destroyAllWindows()


if __name__ == "__main__":

    main()
