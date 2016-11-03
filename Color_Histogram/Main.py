
# directory="C:/Users/Regina/PycharmProjects/MULTIRE_MP1/src_codes/Images"
# searchImage="C:/Users/Regina/PycharmProjects/MULTIRE_MP1/src_codes/Images/1.jpg"

# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
#
# features = []
#
# img = cv2.imread('C:/Users/Regina/PycharmProjects/MULTIRE_MP1/src_codes/Images/1.jpg')
# cv2.imshow('GoldenGate',img)
# hist = cv2.calcHist([img],[0],None,[256],[0,256])
# plt.hist(img.ravel(),256,[0,256])
# plt.title('Histogram for picture')
# plt.show()
#
# features.extend(hist)
# print(features.__sizeof__())
#
# while True:
#     k = cv2.waitKey(0) & 0xFF
#     if k == 27: break             # ESC key to exit
# cv2.destroyAllWindows()

import cv2
import numpy as np
from matplotlib import pyplot as plt

# convert the image to the LUV color space and initialize
# the features used to quantify the image
img = cv2.imread('C:/Users/Regina/PycharmProjects/MULTIRE_MP1/src_codes/Images/1.jpg')

features1= []

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
hist = cv2.normalize(hist, hist).flatten()

features1.extend(hist)

print(features1)

print(features1.__sizeof__())

img_converted = cv2.cvtColor(img, cv2.COLOR_BGR2LUV)

features = []

hist = cv2.calcHist([img_converted], [0], None, [256], [0, 256])
hist = cv2.normalize(hist, hist).flatten()

features.extend(hist)

print(features)

print(features.__sizeof__())


