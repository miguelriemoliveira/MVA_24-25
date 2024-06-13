#!/usr/bin/env python3
# Sistemas Avançados de Visão Industrial (SAVI 22-23)
# Miguel Riem Oliveira, DEM, UA
# Inspired from https://github.com/k-choonkiat/TemplateMatching/tree/master

import sys
from copy import deepcopy

import cv2
import numpy as np


def main():
    image = cv2.imread('../images/scene.jpg')
    template = cv2.imread('../images/wally.png')

    if image is None or template is None:
        sys.exit("Could not read the images.")

    cv2.imshow("Image", image)
    cv2.imshow("Template", template)
    
    #saves the width and height of the template into 'w' and 'h'
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    h, w,_ = template.shape
    H, W = image_gray.shape

    result = cv2.matchTemplate(image_gray,template_gray,cv2.TM_CCOEFF_NORMED)
    threshold = 0.6

    # finding the values where it exceeds the threshold
    loc = np.where( result >= threshold)
    print(list(loc))
    image_result = deepcopy(image)
    for pt in list(loc):
        #draw rectangle on places where it exceeds threshold
        cv2.rectangle(image_result, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
        print('Found a Wally on pt = ' + str(pt))


    # Create a mask with white where the faces were detected
    mask = np.zeros((H,W)).astype(np.uint8)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(mask, pt, (pt[0] + w, pt[1] + h), 255, -1)

    cv2.imshow("Mask", mask)

    # Start from the grayscale image, and paint the face back 
    image_highlighted = cv2.merge([image_gray,image_gray, image_gray])

    image_highlighted_b = deepcopy(image_gray)*0
    image_highlighted[mask] = image[mask]

    image_b, image_g, image_r = cv2.split(image)
    mask = mask.astype(bool)
    # image_highlighted_b[mask] = image_b[mask]
    image_highlighted[mask] = image[mask]


    cv2.imshow("Highlighted", image_highlighted)

    cv2.imshow("Results", image_result)
    cv2.waitKey(0)

print('Terminated.')

if __name__ == "__main__":
    main()
