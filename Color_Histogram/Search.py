# import the necessary packages
from Color_Histogram.ColorDescriptor import ColorDescriptor
from Color_Histogram.Searcher import Searcher
import cv2

from shutil import copy2

# initialize the image descriptor
cd = ColorDescriptor()

# load the query image and describe it
query = cv2.imread("../Images/1367.jpg")
features = cd.describe(query)

# perform the search
searcher = Searcher("Indexed_Images_CH.csv")
results = searcher.search(features)

#open CSV file for writing the results
output = open("../Output/Color Histogram/Results.csv", "w")

# loop over the results
for (score, resultID) in results:
    # load the result image and display it
    output.write("%s,%f\n" % (resultID,score))
    copy2("../" + resultID, "../Output/Color Histogram")

print ("done")
