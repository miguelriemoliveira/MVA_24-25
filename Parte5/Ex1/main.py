#!/usr/bin/env python3
# Sistemas Avançados de Visão Industrial (SAVI 22-23)
# Miguel Riem Oliveira, DEM, UA
# Inspired from https://github.com/k-choonkiat/TemplateMatching/tree/master

import sys
from copy import deepcopy

import cv2
import numpy as np
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


def main():

    # image = cv2.imread('../imagens/lake.jpg')
    image = cv2.imread('../imagens/fruits3.png')
    if image is None:
        sys.exit("Could not read the images.")

    cv2.circle(image, (50, 50), 140, (200, 0, 0), -1)
    cv2.imshow("Image", image)

    H, W, nc = image.shape

    cv2.waitKey(50)

    bs = []
    gs = []
    rs = []
    colors = []
    step = 10
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
    plt.show()


if __name__ == "__main__":
    main()
