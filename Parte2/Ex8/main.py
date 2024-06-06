
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


def main():

    # --------------------------
    # Initialization
    # --------------------------
    # filename = '/home/mike/sharedVBWindows/MVA_6-24/MVA_24-25/Parte1/imagens/grey_lake.jpg'
    filename = '/home/mike/sharedVBWindows/MVA_6-24/MVA_24-25/Parte2/imagens/ireland-06-02.tif'
    if not os.path.isfile(filename):
        print('filename ' + filename + ' does not exist')

    # Load the image
    image = cv2.imread(filename,  cv2.IMREAD_GRAYSCALE)
    h, w = image.shape

    image_stretched = image*0

    # --------------------------
    # Execution
    # --------------------------

    # Stretch the histogram
    minimum, maximum, _, _ = cv2.minMaxLoc(image)

    for x in range(0, w):
        for y in range(0, h):
            image_stretched[y, x] = (image[y, x] - minimum) / (maximum-minimum)*255

    # Compute histograms --------------
    nbins = 128

    # how to compute the values of xs
    # linspace returns the centers of the bins, which we use for plotting
    xs = np.round(np.linspace(0, 255, nbins))
    ys = cv2.calcHist([image], [0], None, [nbins], (0, 256), accumulate=False)
    ys_stretched = cv2.calcHist([image_stretched], [0], None, [nbins], (0, 256), accumulate=False)

    # --------------------------
    # Visualization
    # --------------------------

    # Display the image
    cv2.imshow('Image', image)
    cv2.imshow('Image_stretched', image_stretched)

    # Wait for the user to press a key
    cv2.waitKey(100)

    # matplotlib
    plt.plot(xs, ys, 'b')
    plt.plot(xs, ys_stretched, 'r')

    plt.show()

    # Close all windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
