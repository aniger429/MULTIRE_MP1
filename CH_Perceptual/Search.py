# import the necessary packages
from CH_Perceptual import Searcher
import cv2

from shutil import copy2

# # initialize the image descriptor
# cd = ColorDescriptor()

# load the query image and describe it
query = cv2.imread("C:/Users/Regina/Documents/Python Workspace/MULTIRE_MP1/Images/119.jpg")
# features = cd.describe(query)

Searcher(query)

# # # perform the search
# searcher = Searcher("C:/Users/Regina/Documents/Python Workspace/MULTIRE_MP1/Color_Histogram/Indexed_Images_CH.csv")
# results = searcher.search(features)

# # display the query
# cv2.imshow("Query", query)

# loop over the results
for (score, resultID) in results:
    # load the result image and display it
    # result = cv2.imread("C:/Users/Regina/PycharmProjects/MULTIRE_MP1/src_codes/" + resultID)
    # cv2.imshow(resultID, result)
    copy2("C:/Users/Regina/Documents/Python Workspace/MULTIRE_MP1/"+resultID, "C:/Users/Regina/Documents/Python Workspace/MULTIRE_MP1/Color_Histogram/Output")

# while True:
#     k = cv2.waitKey(0) & 0xFF
#     if k == 27: break
#
# cv2.destroyAllWindows()

print ("done")
