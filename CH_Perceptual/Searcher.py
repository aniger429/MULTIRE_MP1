# import the necessary packages
import numpy as np
import csv
import cv2
import glob
from CH_Perceptual.SSIM import compute_ssim


query = cv2.imread("C:/Users/Regina/Documents/Python Workspace/MULTIRE_MP1/Images/119.jpg")

# initialize our dictionary of results
results = {}

for imagePath in glob.glob("C:/Users/Regina/Documents/Python Workspace/MULTIRE_MP1/Images" + "/*.jpg"):
    # extract the image ID (i.e. the unique filename) from the image
    # path and load the image itself
    imageID = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)

    d = compute_ssim(query, image)

    print(imageID + ":" + d)

# sort our results, so that the smaller distances (i.e. the
# more relevant images are at the front of the list)
# results = sorted([(v, k) for (k, v) in results.items()])

# # return our (limited) results
# return results[:limit]

