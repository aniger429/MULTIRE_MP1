# import the necessary packages
from CH_Center_Refine.ColorDescriptor import ColorDescriptor
from CH_Center_Refine.Searcher import Searcher
import argparse
import cv2

from shutil import copy2

# initialize the image descriptor
cd = ColorDescriptor([8,12,5])

# load the query image and describe it
query = cv2.imread("../Images/1367.jpg")
features = cd.describe(query)

# perform the search
searcher = Searcher("Indexed_Images_CH_Center_Refine.csv")
results = searcher.search(features)

# # display the query
# cv2.imshow("Query", query)

output = open("../Output/Center Refinement/Results.csv", "w")


# loop over the results
for (score, resultID) in results:
    # load the result image and display it
    # result = cv2.imread("C:/Users/Regina/PycharmProjects/MULTIRE_MP1/src_codes/" + resultID)
    # cv2.imshow(resultID, result)
    # copy2("C:/Users/Regina/Documents/Python Workspace/MULTIRE_MP1/"+resultID, "C:/Users/Regina/Documents/Python Workspace/MULTIRE_MP1/CH_Center_Refine/Output")
    print (resultID)
    output.write("%s,%f\n" % (resultID,score))
    copy2("../" + resultID, "../Output/Center Refinement")

print ("done")
