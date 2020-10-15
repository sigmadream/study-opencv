import cv2 as cv
import sys


img_color = cv.imread("./data/image01.jpg", cv.IMREAD_COLOR)
if img_color is None:
    print("이미지 파일을 읽을 수 없습니다.")
    sys.exit(1)


img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)


img_binary = cv.adaptiveThreshold(
    img_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 4
)


cv.imshow("Grayscale", img_gray)
cv.imshow("Binary", img_binary)
cv.waitKey(0)
