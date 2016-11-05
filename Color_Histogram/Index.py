# import the necessary packages
import argparse
import glob

import cv2

from Color_Histogram.ColorDescriptor import ColorDescriptor

# # construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-d", "--dataset", required=True,
#                 help="Path to the directory that contains the images to be indexed")
# ap.add_argument("-i", "--index", required=True,
#                 help="Path to where the computed index will be stored")
# args = vars(ap.parse_args())

# initialize the color descriptor
cd = ColorDescriptor()

# open the output index file for writing
output = open("Indexed_Images_CH.csv", "w")

# use glob to grab the image paths and loop over them
for imagePath in glob.glob("C:/Users/Regina/Documents/Python Workspace/MULTIRE_MP1/Images" + "/*.jpg"):
    # extract the image ID (i.e. the unique filename) from the image
    # path and load the image itself
    imageID = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)

    # describe the image
    features = cd.describe(image)

    # write the features to file
    features = [str(f) for f in features]
    output.write("%s,%s\n" % (imageID, ",".join(features)))


# close the index file
output.close()
print("done indexing")