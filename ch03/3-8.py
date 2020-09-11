import cv2 as cv
import numpy as np


img_color = cv.imread("apple.png", cv.IMREAD_COLOR)


height, width = img_color.shape[:2]

img_gray = np.zeros((height, width), np.uint8)


for y in range(0, height):
    for x in range(0, width):

        b = img_color.item(y, x, 0)
        g = img_color.item(y, x, 1)
        r = img_color.item(y, x, 2)

        gray = int(r * 0.2126 + g * 0.7152 + b * 0.0722)

        img_gray.itemset(y, x, gray)


img_result = cv.cvtColor(img_gray, cv.COLOR_GRAY2BGR)


for y in range(150, 201):
    for x in range(200, 251):

        img_result.itemset(y, x, 0, 0)
        img_result.itemset(y, x, 1, 255)
        img_result.itemset(y, x, 2, 0)

cv.imshow("color", img_color)
cv.imshow("result", img_result)

cv.waitKey(0)

cv.destroyAllWindows()
