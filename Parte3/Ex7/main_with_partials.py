
from copy import deepcopy
from functools import partial
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


# functions

def mouseCallback(event, x, y, flags, param, d):

    if event == cv2.EVENT_LBUTTONDBLCLK:
        print('x= ' + str(x) + ' y=' + str(y))
        d['seed'] = (x, y)

        image_to_flood = d['image']
        d['mask_to_flood'] = d['mask_to_flood']*0
        # run the flood fill
        _, d['image_flooded'], d['mask_flooded'], _ = cv2.floodFill(
            image_to_flood, d['mask_to_flood'], d['seed'], d['new_val'], d['low'], d['up'], d['flags'])


def main():

    # --------------------------
    # Initialization
    # --------------------------
    filename = '/home/mike/sharedVBWindows/MVA_6-24/MVA_24-25/Parte3/imagens/lena.jpg'
    if not os.path.isfile(filename):
        print('filename ' + filename + ' does not exist')

    # Load the image
    image = cv2.imread(filename,  cv2.IMREAD_GRAYSCALE)
    image_flooded = image * 0
    mask_flooded = image * 0

    # prepare flood fill parameters

    d = {}
    d['image'] = image
    d['image_flooded'] = image_flooded
    d['mask_flooded'] = mask_flooded

    d['h'], d['w'] = d['image'].shape

    d['mask_to_flood'] = np.zeros((d['h']+2, d['w']+2), dtype=np.uint8)
    d['seed'] = (0, 0)
    d['new_val'] = 128
    d['low'] = 10
    d['up'] = 10
    d['flags'] = 4 | (d['new_val'] << 8) | cv2.FLOODFILL_MASK_ONLY

    cv2.namedWindow('Image')
    cv2.setMouseCallback('Image', partial(mouseCallback,
                                          d=d))
    cv2.imshow('Image', image)

    # --------------------------
    # Execution
    # --------------------------
    while True:
        cv2.imshow('image_flooded', d['image_flooded'])
        cv2.imshow('mask_flooded', d['mask_flooded'])
        cv2.waitKey(50)
        print(d)

    # Close all windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
