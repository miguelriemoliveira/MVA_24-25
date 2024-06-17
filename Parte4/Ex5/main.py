#!/usr/bin/env python3
# Sistemas Avançados de Visão Industrial (SAVI 22-23)
# Miguel Riem Oliveira, DEM, UA
# Inspired from https://github.com/k-choonkiat/TemplateMatching/tree/master

import sys
from copy import deepcopy

import cv2
import numpy as np


def main():

    # ----------------------------------
    # Initialization
    # ----------------------------------
    original_image = cv2.imread('../imagens/lake.jpg')
    if original_image is None:
        sys.exit("Could not read the image.")

    h, w, _ = original_image.shape

    cv2.imshow("Original Image", original_image)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter('output.avi', fourcc, 20.0, (w, h))

    # ----------------------------------
    # Execution
    # ----------------------------------
    for factor in np.linspace(1.0, 0.0, num=100).tolist():

        # 0. copy from original
        image = deepcopy(original_image)

        # 1. convert image to float
        image_f = image.astype(float)

        # 2. multiply by a factor
        image_f[:, int(w/2):w, :] = image_f[:, int(w/2):w, :] * factor

        # 3. convert the image back to uint8
        image = image_f.astype(np.uint8)

        # 4. record frame to video
        video_writer.write(image)

        cv2.imshow("Image", image)
        cv2.waitKey(50)

    # 1., 2. e 3.
    # image = (image.astype(float) * 0.5).astype(np.uint8)
    # print(image.dtype)


print('Terminated.')

if __name__ == "__main__":
    main()
