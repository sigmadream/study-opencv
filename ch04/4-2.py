import cv2 as cv


def on_trackbar(x):
    pass


cv.namedWindow("Canny")


cv.createTrackbar("low threshold", "Canny", 0, 1000, on_trackbar)
cv.createTrackbar("high threshold", "Canny", 0, 1000, on_trackbar)


cv.setTrackbarPos("low threshold", "Canny", 50)
cv.setTrackbarPos("high threshold", "Canny", 150)


img_gray = cv.imread("orange.png", cv.IMREAD_GRAYSCALE)


while True:

    low = cv.getTrackbarPos("low threshold", "Canny")
    high = cv.getTrackbarPos("high threshold", "Canny")

    img_canny = cv.Canny(img_gray, low, high)

    cv.imshow("Canny", img_canny)

    if cv.waitKey(1) & 0xFF == 27:
        break


cv.destroyAllWindows()
