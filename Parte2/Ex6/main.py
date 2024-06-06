
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

    # results = results.astype(np.uint8)
    return results


def main():

    # ------------------------------------------------------

    # Initialization

    # ------------------------------------------------------

    # TODO Create a black image with 400x600
    filename = '/home/mike/sharedVBWindows/MVA_6-24/MVA_24-25/Parte2/imagens/chess.png'
    if not os.path.isfile(filename):
        print('filename ' + filename + ' does not exist')

    # Load the image
    image = cv2.imread(filename,  cv2.IMREAD_GRAYSCALE)

    # image = np.zeros((500, 500)).astype(np.uint8)
    # image[200:260, 300:400] = 255
    # h, w = image.shape

    # ------------------------------------------------------
    # Execution
    # ------------------------------------------------------
    threshold = 1.5

    # define a filter for detecting vertical edges
    Fx = np.asarray([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]], dtype=float)
    print('Fx=\n' + str(Fx))

    result_x = filter2d(image.astype(float)/255, Fx)

    mask_x = (np.abs(result_x) > threshold).astype(np.uint8)*255

    # define a filter for detecting horizontal edges
    Fy = np.asarray([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]], dtype=float)
    Fy = Fy.transpose()
    print('Fy=\n' + str(Fy))

    result_y = filter2d(image.astype(float)/255, Fy)

    mask_y = (np.abs(result_y) > threshold).astype(np.uint8)*255

    # ------------------------------------------------------
    # Visualization
    # ------------------------------------------------------

    window_name = 'Image'
    # cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    # cv2.resizeWindow(window_name, w*4, h*4)
    cv2.imshow(window_name, image)

    window_name = 'mask_x'
    cv2.imshow(window_name, mask_x)

    window_name = 'mask_y'
    cv2.imshow(window_name, mask_y)

    # Wait for the user to press a key
    cv2.waitKey(0)

    # ------------------------------------------------------
    # Termination
    # ------------------------------------------------------

    # Close all windows
    cv2.destroyAllWindows()


if __name__ == "__main__":

    main()
