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
    cap = cv2.VideoCapture('../imagens/traffic.mp4')

    xtl, ytl = 691, 454
    xbr, ybr = 874, 607
    avg_color_ref = 129.7
    tolerance = 30
    num_cars = 0

    # -------------------------------------
    # Execution
    # -------------------------------------
    while cap.isOpened():
        ret, frame = cap.read()

        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        image_gui = deepcopy(frame)

        # Draw rectangle
        cv2.rectangle(image_gui, (xtl, ytl), (xbr, ybr), (255, 0, 0), 1)

        # extract subimage
        sub_image = image_gray[ytl:ybr, xtl:xbr]

        # get average color
        avg_color = np.mean(sub_image)

        # Draw avg_color on image
        image_gui = cv2.putText(image_gui, str(round(avg_color, 1)), (xtl, ytl-10),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2, cv2.LINE_AA)

        # Change detection
        if avg_color > avg_color_ref + tolerance or avg_color < avg_color_ref - tolerance:  # change detected
            num_cars += 1

        image_gui = cv2.putText(image_gui, 'num_cars = ' + str(num_cars), (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow('Image GUI', image_gui)
        # cv2.imshow('sub_image', sub_image)
        if cv2.waitKey(0) == ord('q'):
            break

    # -------------------------------------
    # Termination
    # -------------------------------------
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
