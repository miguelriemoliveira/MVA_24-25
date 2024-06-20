import cv2

import numpy as np


def ShowImage(NameWindow, Image):

    cv2.namedWindow(str(NameWindow))

    cv2.imshow(str(NameWindow), Image)


def Main():

    rows = 400

    cols = 600

    Image = cv2.cvtColor(np.zeros((rows, cols)).astype(np.uint8), cv2.COLOR_GRAY2BGR)

    Image = cv2.circle(Image, (200, 100), 50, (0, 0, 255), -1)

    Image = cv2.rectangle(Image, (350, 50), (450, 150), (0, 255, 0), -1)

    Image = cv2.circle(Image, (300, 300), 50, (0, 255, 255), -1)

    ShowImage('Image', Image)

    cv2.waitKey(0)

    cv2.destroyAllWindows()


if __name__ == "__main__":

    Main()
