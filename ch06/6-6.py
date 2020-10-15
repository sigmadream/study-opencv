import cv2 as cv
import numpy as np


img_logo = cv.imread("./data/logo.png", cv.IMREAD_COLOR)
img_background = cv.imread("./data/background.png", cv.IMREAD_COLOR)


img_gray = cv.cvtColor(img_logo, cv.COLOR_BGR2GRAY)
ret, img_mask = cv.threshold(img_gray, 200, 255, cv.THRESH_BINARY)


img_mask_inv = cv.bitwise_not(img_mask)


height, width = img_logo.shape[:2]
img_roi = img_background[0:height, 0:width]


img1 = cv.bitwise_and(img_logo, img_logo, mask=img_mask_inv)
img2 = cv.bitwise_and(img_roi, img_roi, mask=img_mask)


dst = cv.add(img1, img2)


img_background[0:height, 0:width] = dst


# cv.imshow("background", img_background)
# cv.imshow('logo', img_logo)
# cv.imshow("img_mask_inv", img_mask_inv)
# cv.imshow('img_mask', img_mask)
# cv.imshow('img1', img1)
# cv.imshow('img2', img2)
# cv.imshow('dst', dst)
cv.waitKey(0)
