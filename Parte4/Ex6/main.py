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
    prev_flg_out_of_tolerance = None
    frame_number = 0
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

        image_gui = cv2.putText(image_gui, 'frame = ' +
                                str(frame_number), (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255),
                                2, cv2.LINE_AA)

        # out of tolerance
        flg_out_of_tolerance = False
        if avg_color > avg_color_ref + tolerance or avg_color < avg_color_ref - tolerance:  # change detected
            flg_out_of_tolerance = True

        image_gui = cv2.putText(image_gui, 'out_of_tolerance = ' +
                                str(flg_out_of_tolerance), (10, 60),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255),
                                2, cv2.LINE_AA)

        # rising edge detection
        flg_rising_edge = False
        if prev_flg_out_of_tolerance is not None:
            if not prev_flg_out_of_tolerance and flg_out_of_tolerance:
                flg_rising_edge = True

        image_gui = cv2.putText(image_gui, 'rising_edge = ' +
                                str(flg_rising_edge), (10, 90),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255),
                                2, cv2.LINE_AA)

        # car count
        if flg_rising_edge:
            num_cars += 1

        image_gui = cv2.putText(image_gui, 'num_cars = ' + str(num_cars), (10, 120),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow('Image GUI', image_gui)
        # cv2.imshow('sub_image', sub_image)
        if cv2.waitKey(30) == ord('q'):
            break

        prev_flg_out_of_tolerance = flg_out_of_tolerance
        frame_number += 1

    # -------------------------------------
    # Termination
    # -------------------------------------
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
