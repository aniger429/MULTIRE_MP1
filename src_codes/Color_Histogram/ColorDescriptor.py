# import the necessary packages
import numpy as np
import cv2


class ColorDescriptor:
    def describe(self, image):
        # convert the image to the HSV color space and initialize
        # the features used to quantify the image
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2LUV)
        features = []

        # extract a color histogram from the elliptical region and
        # update the feature vector

        hist = self.histogram(image)
        features.extend(hist)

        # return the feature vector
        return features

    def histogram(self, image):
        # extract a 3D color histogram from the masked region of the
        # image, using the supplied number of bins per channel; then
        # normalize the histogram
        hist = cv2.calcHist([image], [0, 1, 2], None, [8,8,8], [0, 256, 0, 256, 0, 256])
        hist = cv2.normalize(hist,hist).flatten()

        # return the histogram
        return hist