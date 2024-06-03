
import random
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


def filter2d(image, filter):

    h, w = image.shape  # get width and height
    results = (image*0).astype(float)  # create results same size as image
    for x in range(1, w-1):
        for y in range(1, h-1):
            subimage = (image[y-1:y+2, x-1:x+2]).astype(float)
            subres = np.multiply(subimage, filter)
            som_subres = np.sum(subres)
            results[y, x] = som_subres

    results = results.astype(np.uint8)
    return results


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
    image = np.zeros((500, 500)).astype(np.uint8)
    image[200:260, 300:400] = 255
    h, w = image.shape

    # ------------------------------------------------------
    # Execution
    # ------------------------------------------------------

    # add noise
    flip_flop = False  # init flip_flop
    for x in range(0, w):
        for y in range(0, h):
            if random.random() > (1-0.2):  # add noise
                if flip_flop:  # paint white (salt)
                    image[y, x] = 255
                else:  # paint black (pepper)
                    image[y, x] = 0
                flip_flop = not flip_flop  # invert flip flop

    # Filtering
    # F = np.ones((3, 3), dtype=float)*(1/9)  # equivalente a filtro de media
    F = np.ones((3, 3), dtype=float)*-1
    F[1, 1] = 8  # filtro pontos isolados
    print('F=\n' + str(F))

    result = filter2d(image/255, F)

    mask_iso = (result == 8).astype(np.uint8)*255

    window_name = 'original'
    cv2.imshow(window_name, image)

    window_name = 'resultado'
    cv2.imshow(window_name, result)

    window_name = 'mask_iso'
    cv2.imshow(window_name, mask_iso)

    # Wait for the user to press a key
    cv2.waitKey(0)

    # ------------------------------------------------------
    # Termination
    # ------------------------------------------------------

    # Close all windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
