import cv2 as cv


img_background = cv.imread("./data/image01.jpg", cv.IMREAD_GRAYSCALE)
img_object = cv.imread("./data/image01_gray.jpg", cv.IMREAD_GRAYSCALE)


img_sub = cv.subtract(img_object, img_background)


retval, img_binary = cv.threshold(img_sub, 50, 255, cv.THRESH_BINARY)


cv.imshow("background", img_background)
cv.imshow("object", img_object)
cv.imshow("sub", img_sub)
cv.imshow("binary", img_binary)
cv.waitKey(0)