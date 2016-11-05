# import the necessary packages
import numpy as np
import cv2


class ColorDescriptor:
    def __init__(self, bins):
        # store the number of bins for the 3D histogram
        self.bins = bins

    def describe(self, image):
        # convert the image to the HSV color space and initialize
        # the features used to quantify the image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2LUV)
        features = []

        # grab the dimensions and compute the center of the image
        (h, w) = image.shape[:2]
        (cX, cY) = (int(w * 0.5), int(h * 0.5))

        tX = int(cX / 2)
        tY = int(cY / 2)
        bX = int((cX / 2) + cX)
        bY = int((cY / 2) + cY)

        # construct an elliptical mask representing the center of the
        # image
        centerMask = np.zeros(image.shape[:2], dtype="uint8")
        fullImageMask = np.zeros(image.shape[:2], dtype="uint8")

        cv2.rectangle(centerMask, (tX, tY), (bX, bY), 255, -1)
        cv2.rectangle(fullImageMask, (0, 0), (w, h), 255, -1)

        image_mask = cv2.subtract(fullImageMask, centerMask)

        histNoCenter = self.histogram(image, image_mask)
        features.extend(histNoCenter)

        histCenter = self.histogram(image, centerMask)
        features.extend(histCenter)

        # return the feature vector
        return features

    def histogram(self, image, mask):
        # extract a 3D color histogram from the masked region of the
        # image, using the supplied number of bins per channel; then
        # normalize the histogram
        hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins,
                            [0, 180, 0, 256, 0, 256])
        hist = cv2.normalize(hist, hist).flatten()

        # return the histogram
        return hist