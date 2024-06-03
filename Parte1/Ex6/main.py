
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


def main():

    # filename = '/home/mike/sharedVBWindows/MVA_6-24/MVA_24-25/Parte1/imagens/grey_lake.jpg'
    filename = '/home/mike/sharedVBWindows/MVA_6-24/MVA_24-25/Parte1/imagens/chess.png'

    if not os.path.isfile(filename):
        print('filename ' + filename + ' does not exist')

    # Load the image
    image = cv2.imread(filename,  cv2.IMREAD_GRAYSCALE)

    # compute histogram
    nbins = 128

    # how to compute the values of xs
    # linspace returns the centers of the bins, which we use for plotting
    xs = np.round(np.linspace(0, 255, nbins))

    ys = cv2.calcHist([image], [0], None, [nbins], (0, 256), accumulate=False)

    print(ys)
    print(len(ys))

    print(xs)
    print(len(xs))

    # Display the image
    cv2.imshow('Image', image)

    # thresholding

    # Get white and grey squares
    bw = (image > 90).astype(np.uint8)*255
    print(bw.dtype)
    cv2.imshow('gray and white', bw)

    # Get black and grey squares
    bw2 = (image < 190).astype(np.uint8)*255
    cv2.imshow('black and gray', bw2)

    # Get black and grey squares
    # bw3 = (image > 190).astype(np.uint8)*255
    bw3 = (np.logical_not(image < 190)).astype(np.uint8)*255
    cv2.imshow('whites', bw3)

    # Wait for the user to press a key
    cv2.waitKey(100)

    # matplotlib
    plt.plot(xs, ys)
    plt.show()

    # Close all windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
