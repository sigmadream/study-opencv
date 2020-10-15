import cv2 as cv
import sys


def on_trackbar(x):
    pass


img_color = cv.imread("./data/image01.jpg", cv.IMREAD_COLOR)
if img_color is None:
    print("이미지 파일을 읽을 수 없습니다.")
    sys.exit(1)


img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", img_gray)


cv.namedWindow("Binary")
cv.createTrackbar("threshold", "Binary", 0, 255, on_trackbar)
cv.setTrackbarPos("threshold", "Binary", 127)


while True:

    thresh = cv.getTrackbarPos("threshold", "Binary")

    retval, img_binary = cv.threshold(img_gray, thresh, 255, cv.THRESH_BINARY_INV)

    cv.imshow("Binary", img_binary)

    if cv.waitKey(1) & 0xFF == 27:
        break
