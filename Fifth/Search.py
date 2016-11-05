# import the necessary packages
from Fifth.ColorDescriptor import ColorDescriptor
from Fifth.Searcher import Searcher
import cv2

from shutil import copy2

# initialize the image descriptor
cd = ColorDescriptor((8,12,5))

# load the query image and describe it
query = cv2.imread("../Images/119.jpg")
features = cd.describe(query)

# perform the search
searcher = Searcher("Indexed_Images.csv")
results = searcher.search(features)

#open CSV file for writing the results
output = open("../Output/Bonus/Results.csv", "w")

# loop over the results
for (score, resultID) in results:
    # load the result image and display it
    output.write("%s,%f\n" % (resultID,score))
    copy2("../" + resultID, "../Output/Bonus")

print ("done")
