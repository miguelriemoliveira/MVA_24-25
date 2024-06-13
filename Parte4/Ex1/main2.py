#!/usr/bin/env python3
# Sistemas Avançados de Visão Industrial (SAVI 22-23)
# Miguel Riem Oliveira, DEM, UA
# Inspired from https://github.com/k-choonkiat/TemplateMatching/tree/master

import random
import sys
from copy import deepcopy

import cv2
import numpy as np


def main():

    # ----------------------------------------------
    # Initialization
    # ----------------------------------------------
    image = cv2.imread('../imagens/scene.jpg')
    # image = cv2.imread('../imagens/school.jpg')
    # template = cv2.imread('../imagens/wally.png')
    # template = cv2.imread('../imagens/bison_template3.png')
    template = cv2.imread('../imagens/bison_template4.png')
    if image is None or template is None:
        sys.exit("Could not read the images.")

    H, W, _ = image.shape
    h, w, _ = template.shape
    aspect_ratio = w/h

    # aspect_ratio = w/h
    # w = aspect_ratio * h
    image_gui = deepcopy(image)

    # Test of resizing
    # resized_template = cv2.resize(template, (int(aspect_ratio*40), 40),
    #                               interpolation=cv2.INTER_LINEAR)

    # cv2.imshow("Template", template)
    # cv2.imshow("Template resized", resized_template)
    # cv2.waitKey(0)

    # ----------------------------------------------
    # Execution
    # ----------------------------------------------
    best = {'max_loc': None, 'max_val': None, 'wi': None, 'hi': None}

    hs = [h-x for x in range(0,  80, 25)]
    ws = [int(aspect_ratio*i) for i in hs]
    for hi, wi in zip(hs, ws):

        # Test of resizing
        template_i = cv2.resize(template, (wi, hi), interpolation=cv2.INTER_LINEAR)

        result = cv2.matchTemplate(image=image, templ=template_i, method=cv2.TM_CCORR_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if best['max_val'] is None or max_val > best['max_val']:
            # if max_val > best['max_val'] or best['max_val'] is None:
            best['max_loc'] = max_loc
            best['max_val'] = max_val
            best['wi'] = wi
            best['hi'] = hi

    print('Max correlation is ' + str(best['max_val']))
    xi = best['max_loc'][0]
    yi = best['max_loc'][1]
    xf = best['max_loc'][0] + best['wi']
    yf = best['max_loc'][1] + best['hi']
    cv2.rectangle(image_gui, (xi, yi), (xf, yf), (random.randint(0, 255),
                                                  random.randint(0, 255),
                                                  random.randint(0, 255)), 2)

    cv2.imshow("Image", image_gui)
    cv2.imshow("Template", template)
    cv2.imshow('result', (result*255).astype(np.uint8))
    cv2.waitKey(0)


# ----------------------------------------------
# Termination
# ----------------------------------------------
if __name__ == "__main__":
    main()
