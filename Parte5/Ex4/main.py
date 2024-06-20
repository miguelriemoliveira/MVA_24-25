#!/usr/bin/env python3
# Sistemas Avançados de Visão Industrial (SAVI 22-23)
# Miguel Riem Oliveira, DEM, UA
# Inspired from https://github.com/k-choonkiat/TemplateMatching/tree/master

from functools import partial
import sys
from copy import deepcopy
import json
import cv2
import numpy as np
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


# def trackbarCallback(value, color, max_or_min):
# pass

def trackbar_rmin(value, color_limits):
    print('Changed trackbar rmin value to ' + str(value))
    color_limits['rmin'] = value


def trackbar_rmax(value, color_limits):
    print('Changed trackbar rmax value to ' + str(value))
    color_limits['rmax'] = value


def trackbar_gmin(value, color_limits):
    print('Changed trackbar gmin value to ' + str(value))
    color_limits['gmin'] = value


def trackbar_gmax(value, color_limits):
    print('Changed trackbar gmax value to ' + str(value))
    color_limits['gmax'] = value


def trackbar_bmin(value, color_limits):
    print('Changed trackbar bmin value to ' + str(value))
    color_limits['bmin'] = value


def trackbar_bmax(value, color_limits):
    print('Changed trackbar bmax value to ' + str(value))
    color_limits['bmax'] = value


def main():

    # image = cv2.imread('../imagens/lake.jpg')
    image = cv2.imread('../imagens/castle.png')
    if image is None:
        sys.exit("Could not read the images.")

    cv2.namedWindow('Image', cv2.WINDOW_GUI_NORMAL)
    cv2.imshow("Image", image)

    H, W, nc = image.shape

    cv2.waitKey(50)

    bs = []
    gs = []
    rs = []
    colors = []
    step = 80
    for row in range(0, H, step):
        for col in range(0, W, step):
            bs.append(image[row, col, 0])
            gs.append(image[row, col, 1])
            rs.append(image[row, col, 2])
            color = (image[row, col, 2]/255.0, image[row, col,
                     1]/255.0, image[row, col, 0]/255.0, 1.0)
            colors.append(color)

    # Creating figure
    fig = plt.figure(figsize=(10, 7))
    ax = plt.axes(projection="3d")

    # Creating plot
    ax.scatter3D(rs, gs, bs, color=colors)
    plt.title("simple 3D scatter plot")
    ax.set_xlabel('Red')
    ax.set_ylabel('Green')
    ax.set_zlabel('Blue')

    # show plot
    # plt.show()

    # Segment color
    # Opening JSON file
    with open('color_limits.json', 'r') as infile:
        color_limits = json.load(infile)

    # color_limits = {'gmin': 0, 'gmax': 255, 'rmin': 0, 'rmax': 255, 'bmin': 0, 'bmax': 255}

    # Create the trackbars
    cv2.namedWindow('Mask', cv2.WINDOW_GUI_NORMAL)
    cv2.createTrackbar('rmin', 'Mask', 0, 255, partial(trackbar_rmin, color_limits=color_limits))
    cv2.setTrackbarPos('rmin', 'Mask', color_limits['rmin'])

    cv2.createTrackbar('rmax', 'Mask', 0, 255, partial(trackbar_rmax, color_limits=color_limits))
    cv2.setTrackbarPos('rmax', 'Mask', color_limits['rmax'])

    cv2.createTrackbar('gmin', 'Mask', 0, 255, partial(trackbar_gmin, color_limits=color_limits))
    cv2.setTrackbarPos('gmin', 'Mask', color_limits['gmin'])

    cv2.createTrackbar('gmax', 'Mask', 0, 255, partial(trackbar_gmax, color_limits=color_limits))
    cv2.setTrackbarPos('gmax', 'Mask', color_limits['gmax'])

    cv2.createTrackbar('bmin', 'Mask', 0, 255, partial(trackbar_bmin, color_limits=color_limits))
    cv2.setTrackbarPos('bmin', 'Mask', color_limits['bmin'])

    cv2.createTrackbar('bmax', 'Mask', 0, 255, partial(trackbar_bmax, color_limits=color_limits))
    cv2.setTrackbarPos('bmax', 'Mask', color_limits['bmax'])

    # split channels
    R, G, B = cv2.split(image)
    # R = image[:,:,2]

    while True:
        # Color segmentation
        mask_R = np.logical_and(R >= color_limits['rmin'],  R <= color_limits['rmax'])
        mask_G = np.logical_and(G >= color_limits['gmin'],  G <= color_limits['gmax'])
        mask_B = np.logical_and(B >= color_limits['bmin'],  B <= color_limits['bmax'])

        mask = np.logical_and(np.logical_and(mask_R, mask_G), mask_B)

        # Visualziation
        cv2.imshow("Mask", mask.astype(np.uint8)*255)
        key = cv2.waitKey(100)
        if key == 113:  # tecla "q"
            break

    with open('color_limits.json', 'w') as outfile:
        json.dump(color_limits, outfile, indent=4)


if __name__ == "__main__":
    main()
