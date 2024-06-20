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

    image = cv2.imread('../imagens/lake.jpg')
    # image = cv2.imread('../imagens/castle.png')
    # image = cv2.imread('../imagens/fruits3.png')
    if image is None:
        sys.exit("Could not read the images.")

    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    image_hsv = image_hsv.astype(float)

    image_hsv[:, :, 2] = image_hsv[:, :, 2] * 1.8
    image_hsv[:, :, 1] = image_hsv[:, :, 1] * 1.8
    image_hsv = np.where(image_hsv > 255, 255, image_hsv)
    image_hsv = image_hsv.astype(np.uint8)

    image_rgb2 = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)

    cv2.namedWindow('Image', cv2.WINDOW_GUI_NORMAL)
    cv2.imshow("Image", image)

    cv2.namedWindow('Image HSV', cv2.WINDOW_GUI_NORMAL)
    cv2.imshow('Image HSV', image_hsv)

    cv2.namedWindow('Image RGB2', cv2.WINDOW_GUI_NORMAL)
    cv2.imshow("Image RGB2", image_rgb2)

    cv2.waitKey(0)


if __name__ == "__main__":
    main()
