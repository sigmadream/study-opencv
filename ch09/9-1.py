import cv2

img_color = cv2.imread("./data/image01.jpg")
cv2.imshow("color", img_color)


height, width = img_color.shape[:2]


M = cv2.getRotationMatrix2D((width / 2.0, height / 2.0), 45, 1)

img_rotated = cv2.warpAffine(img_color, M, (width, height))

cv2.imshow("rotation", img_rotated)
cv2.waitKey(0)

cv2.destroyAllWindows()
