import cv2 as cv
import sys


img_color = cv.imread("./data/image01.jpg", cv.IMREAD_COLOR)


if img_color is None:
    print("이미지 파일을 읽을 수 없습니다.")
    sys.exit(1)


img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

img_canny = cv.Canny(img_gray, 90, 180)


cv.imshow("Grayscale", img_gray)
cv.imshow("Canny", img_canny)

cv.waitKey(0)
cv.destroyAllWindows()
