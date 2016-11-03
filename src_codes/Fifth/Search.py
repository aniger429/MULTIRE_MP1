# import the necessary packages
from src_codes.Fifth.ColorDescriptor import ColorDescriptor
from src_codes.Fifth.Searcher import Searcher
import argparse
import cv2

from shutil import copy2
#
# # construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--index", required=True,
#                 help="Path to where the computed index will be stored")
# ap.add_argument("-q", "--query", required=True,
#                 help="Path to the query image")
# ap.add_argument("-r", "--result-path", required=True,
#                 help="Path to the result path")
# args = vars(ap.parse_args())

# initialize the image descriptor
cd = ColorDescriptor((8, 12, 3))

# load the query image and describe it
query = cv2.imread("C:/Users/Regina/PycharmProjects/MULTIRE_MP1/src_codes/Images/1795.jpg")
features = cd.describe(query)

# perform the search
searcher = Searcher("C:/Users/Regina/PycharmProjects/MULTIRE_MP1/src_codes/Fifth/Indexed_Images.csv")
results = searcher.search(features)

# # display the query
# cv2.imshow("Query", query)

# loop over the results
for (score, resultID) in results:
    # load the result image and display it
    # result = cv2.imread("C:/Users/Regina/PycharmProjects/MULTIRE_MP1/src_codes/" + resultID)
    # cv2.imshow(resultID, result)
    copy2("C:/Users/Regina/PycharmProjects/MULTIRE_MP1/src_codes/"+resultID, "C:/Users/Regina/PycharmProjects/MULTIRE_MP1/src_codes/Output")

# while True:
#     k = cv2.waitKey(0) & 0xFF
#     if k == 27: break
#
# cv2.destroyAllWindows()

print ("done")
