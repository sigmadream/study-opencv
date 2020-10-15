import cv2 as cv
import numpy as np


img_color = cv.imread("./data/image01.jpg")
cv.imshow("original", img_color)


height, width = img_color.shape[:2]


M = np.float32([[1, 0, 100], [0, 1, 50]])


img_translation = cv.warpAffine(img_color, M, (width, height))

cv.imshow("translation", img_translation)


cv.waitKey(0)
cv.destroyAllWindows()