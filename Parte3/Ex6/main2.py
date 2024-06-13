
from copy import deepcopy
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


def main():

    # --------------------------
    # Initialization
    # --------------------------
    filename = '/home/mike/sharedVBWindows/MVA_6-24/MVA_24-25/Parte3/imagens/lena.jpg'
    if not os.path.isfile(filename):
        print('filename ' + filename + ' does not exist')

    # Load the image
    # image = np.zeros((200, 400), dtype=np.uint8)
    # image[:, 200:] = 255
    image = cv2.imread(filename,  cv2.IMREAD_GRAYSCALE)

    _, bw = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
    h, w = image.shape

    # --------------------------
    # Execution
    # --------------------------

    # --------------------------
    # prepare flçood fill parameters
    # --------------------------

    # image	Input/output 1- or 3-channel, 8-bit, or floating-point image. It is modified by the function unless the FLOODFILL_MASK_ONLY flag is set in the second variant of the function. See the details below.
    image_to_flood = image

    # mask	Operation mask that should be a single-channel 8-bit image, 2 pixels wider and 2 pixels taller than image. If an empty Mat is passed it will be created automatically. Since this is both an input and output parameter, you must take responsibility of initializing it. Flood-filling cannot go across non-zero pixels in the input mask. For example, an edge detector output can be used as a mask to stop filling at edges. On output, pixels in the mask corresponding to filled pixels in the image are set to 1 or to the specified value in flags as described below. Additionally, the function fills the border of the mask with ones to simplify internal processing. It is therefore possible to use the same mask in multiple calls to the function to make sure the filled areas do not overlap.
    edges = cv2.Canny(image, 230, 240)

    mask_to_flood = np.zeros((h+2, w+2), dtype=np.uint8)
    # mask_to_flood[1:h+1, 1:w+1] = edges

    mask_to_flood[int(h/2), :] = 255

    # seedPoint	Starting point.
    seed = (273, 124)

    # newVal	New value of the repainted domain pixels.
    new_val = 128

    # loDiff	Maximal lower brightness/color difference between the currently observed pixel and one of its neighbors belonging to the component, or a seed pixel being added to the component.
    low = 10

    # upDiff	Maximal upper brightness/color difference between the currently observed pixel and one of its neighbors belonging to the component, or a seed pixel being added to the component.
    up = 10

    # rect	Optional output parameter set by the function to the minimum bounding rectangle of the repainted domain.

    # flags	Operation flags. The first 8 bits contain a connectivity value. The default value of 4 means that only the four nearest neighbor pixels (those that share an edge) are considered. A connectivity value of 8 means that the eight nearest neighbor pixels (those that share a corner) will be considered. The next 8 bits (8-16) contain a value between 1 and 255 with which to fill the mask (the default value is 1). For example, 4 | ( 255 << 8 ) will consider 4 nearest neighbours and fill the mask with a value of 255. The following additional options occupy higher bits and therefore may be further combined with the connectivity and mask fill values using bit-wise or (|), see FloodFillFlags.\
    # flags = 4 | (new_val << 8) | cv2.FLOODFILL_MASK_ONLY | cv2.FLOODFILL_FIXED_RANGE
    flags = 4 | (new_val << 8) | cv2.FLOODFILL_MASK_ONLY

    # run the flood fill
    retval, image_flodded, mask_flooded, rect = cv2.floodFill(image_to_flood, mask_to_flood,
                                                              seed, new_val, low, up, flags)

    # --------------------------
    # Visualization
    # --------------------------
    # cv2.imshow('Image', image)
    cv2.imshow('bw', bw)
    cv2.imshow('edges', edges)

    cv2.imshow('image_to_flood', image_to_flood)
    cv2.imshow('mask_to__flood', mask_to_flood)
    cv2.imshow('image_flooded', image_flodded)
    cv2.imshow('mask_flooded', mask_flooded)
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
