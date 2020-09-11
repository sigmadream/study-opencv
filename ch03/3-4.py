import cv2 as cv


img_gray = cv.imread("./data/image01.jpg", cv.IMREAD_GRAYSCALE)

img_sub1 = img_gray[: 20 + 150, : 20 + 150]

print(img_sub1.base is img_gray)


cv.line(img_sub1, (0, 0), (100, 100), 0, 10)


ret, img_sub1 = cv.threshold(img_sub1, 127, 255, cv.THRESH_BINARY)

print(img_sub1.base is img_gray)


cv.imshow("img_gray", img_gray)
cv.imshow("img_sub1", img_sub1)

cv.waitKey(0)
