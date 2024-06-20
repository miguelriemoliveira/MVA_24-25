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

def trackbar(value, color_limits, color_key):
    print('Changed trackbar ' + color_key+' value to ' + str(value))
    color_limits[color_key] = value


def main():

    # image = cv2.imread('../imagens/lake.jpg')
    # image = cv2.imread('../imagens/castle.png')
    image = cv2.imread('../imagens/fruits3.png')
    if image is None:
        sys.exit("Could not read the images.")

    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    cv2.namedWindow('Image', cv2.WINDOW_GUI_NORMAL)
    cv2.imshow("Image", image)

    cv2.namedWindow('Image HSV', cv2.WINDOW_GUI_NORMAL)
    cv2.imshow('Image HSV', image_hsv)

    H, W, nc = image.shape

    cv2.waitKey(50)

    # Segment color
    # Opening JSON file
    with open('color_limits.json', 'r') as infile:
        color_limits = json.load(infile)

    # Create the trackbars
    cv2.namedWindow('Mask', cv2.WINDOW_GUI_NORMAL)
    cv2.createTrackbar('hmin', 'Mask', 0, 180, partial(
        trackbar, color_limits=color_limits, color_key='hmin'))
    cv2.setTrackbarPos('hmin', 'Mask', color_limits['hmin'])

    cv2.createTrackbar('hmax', 'Mask', 0, 180, partial(
        trackbar, color_limits=color_limits, color_key='hmax'))
    cv2.setTrackbarPos('hmax', 'Mask', color_limits['hmax'])

    cv2.createTrackbar('smin', 'Mask', 0, 255, partial(
        trackbar, color_limits=color_limits, color_key='smin'))
    cv2.setTrackbarPos('smin', 'Mask', color_limits['smin'])

    cv2.createTrackbar('smax', 'Mask', 0, 255, partial(
        trackbar, color_limits=color_limits, color_key='smax'))
    cv2.setTrackbarPos('smax', 'Mask', color_limits['smax'])

    cv2.createTrackbar('vmin', 'Mask', 0, 255, partial(
        trackbar, color_limits=color_limits, color_key='vmin'))
    cv2.setTrackbarPos('vmin', 'Mask', color_limits['vmin'])

    cv2.createTrackbar('vmax', 'Mask', 0, 255, partial(
        trackbar, color_limits=color_limits, color_key='vmax'))
    cv2.setTrackbarPos('vmax', 'Mask', color_limits['vmax'])

    # split channels
    H, S, V = cv2.split(image_hsv)
    # R = image[:,:,2]

    while True:
        # Color segmentation
        # mask_H = np.logical_and(H <= color_limits['hmin'],  H >= color_limits['hmax'])

        mask_H = np.logical_or(H >= color_limits['hmin'],  H <= color_limits['hmax'])
        mask_S = np.logical_and(S >= color_limits['smin'],  S <= color_limits['smax'])
        mask_V = np.logical_and(V >= color_limits['vmin'],  V <= color_limits['vmax'])

        mask = np.logical_and(np.logical_and(mask_H, mask_S), mask_V)

        # Visualziation
        cv2.imshow("Mask", mask.astype(np.uint8)*255)
        key = cv2.waitKey(100)
        if key == 113:  # tecla "q"
            break

    with open('color_limits.json', 'w') as outfile:
        json.dump(color_limits, outfile, indent=4)


if __name__ == "__main__":
    main()
