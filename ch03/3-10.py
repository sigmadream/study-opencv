import cv2 as cv


img_color = cv.imread("./data/image01.jpg", cv.IMREAD_COLOR)


img_b, img_g, img_r = cv.split(img_color)

img_result = cv.merge((img_r, img_g, img_b))


cv.imshow("Color", img_result)
cv.imshow("B", img_b)
cv.imshow("G", img_g)
cv.imshow("R", img_r)

cv.waitKey(0)
cv.destroyAllWindows()
