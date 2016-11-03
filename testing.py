import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("C:/Users/Regina/PycharmProjects/MULTIRE_MP1/src_codes/Images/100.jpg")
color = ('b','g','r')

for i, col in enumerate(color):
    histr = cv2.calcHist([image],[i], None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])

# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
# cv2.imshow("Gray", gray_image)


# plt.hist(image.ravel(),256,[0,256])
plt.title('Histogram')
plt.show()

while True:
    k = cv2.waitKey(0) & 0xFF
    if k == 27: break

cv2.destroyAllWindows()