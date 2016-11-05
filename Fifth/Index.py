# import the necessary packages
import argparse
import glob
import cv2
from Fifth.ColorDescriptor import ColorDescriptor

cd = ColorDescriptor((8, 12, 5))

# open the output index file for writing
output = open("Indexed_Images.csv", "w")

# use glob to grab the image paths and loop over them
for imagePath in glob.glob("../Images" + "/*.jpg"):
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

print ("done")