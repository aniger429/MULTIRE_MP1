# import the necessary packages
import argparse
import glob

import cv2
from CH_Perceptual import *

# # initialize the color descriptor
# cd = ColorDescriptor()
#
# open the output index file for writing
output = open("Indexed_Images_CH_Perceptual.csv", "w")

query = cv2.imread("C:/Users/Regina/Documents/Python Workspace/MULTIRE_MP1/Images/119.jpg")

# use glob to grab the image paths and loop over them
for imagePath in glob.glob("C:/Users/Regina/Documents/Python Workspace/MULTIRE_MP1/Images" + "/*.jpg"):
    # extract the image ID (i.e. the unique filename) from the image
    # path and load the image itself
    imageID = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)

    # # describe the image
    # features = cd.describe(image)


    # write the features to file
    features = [str(f) for f in features]
    output.write("%s,%s\n" % (imageID, ",".join(features)))


# close the index file
output.close()
print("done indexing")