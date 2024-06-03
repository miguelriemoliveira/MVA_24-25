
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


def main():

    filename = '/home/mike/sharedVBWindows/MVA_6-24/MVA_24-25/Parte1/imagens/grey_lake.jpg'

    if not os.path.isfile(filename):
        print('filename ' + filename + ' does not exist')

    # Load the image
    image = cv2.imread(filename,  cv2.IMREAD_GRAYSCALE)

    # compute histogram
    nbins = 10
    ys = cv2.calcHist(image, [0], None, [nbins], (0, 256), accumulate=False)

    print(ys)
    print(len(ys))

    # how to compute the values of xs
    # linspace returns the centers of the bins, which we use for plotting
    xs = np.linspace(0, 255, nbins)

    print(xs)
    print(len(xs))

    # matplotlib
    plt.plot(xs, ys)
    plt.show()

    # Display the image
    cv2.imshow('Image', image)

    # Wait for the user to press a key
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
