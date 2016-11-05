
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

# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
# from PIL import Image
#
# # convert the image to the LUV color space and initialize
# # the features used to quantify the image
# img = cv2.imread('C:/Users/Regina/Documents/Python Workspace/MULTIRE_MP1/Images/1.jpg')
# img_converted = cv2.cvtColor(img, cv2.COLOR_BGR2LUV)
#
# height, width = img_converted.shape[:2]
#
# features1= []
#
# hist = cv2.calcHist([img_converted], [0, 1, 2], None, [8,12,5], [0, 256, 0, 256, 0, 256])
# hist = cv2.normalize(hist, hist).flatten()
#
# features1.extend(hist)
#
# print (width)
# print (height)

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('C:/Users/Regina/PycharmProjects/MULTIRE_MP1/src_codes/Images/0.jpg',0)

# create a mask
# grab the dimensions and compute the center of the image
(h, w) = image.shape[:2]
(cX, cY) = (int(w * 0.5), int(h * 0.5))

tX = int(cX/2)
tY = int(cY/2)
bX = int((cX/2)+cX)
bY = int((cY/2)+cY)

# construct an  mask representing the center of the
# image
Mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(Mask, (tX, tY), (bX, bY), 255, -1)

masked_img = cv2.bitwise_and(image,image,mask = Mask)
# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([image],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([image],[0],Mask,[256],[0,256])

plt.subplot(221), plt.imshow(image)
plt.subplot(222), plt.imshow(Mask,'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])

plt.show()