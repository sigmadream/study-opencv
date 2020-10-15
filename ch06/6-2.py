import cv2 as cv


alpha = 0.0
beta = 1.0

while alpha <= 1.0:

    img1 = cv.imread("./data/image01.jpg", cv.IMREAD_COLOR)
    img2 = cv.imread("./data/image01_gray.jpg", cv.IMREAD_COLOR)

    dst = cv.addWeighted(img1, alpha, img2, beta, 0)

    print(alpha, " ", beta)

    cv.imshow("dst", dst)
    cv.waitKey(0)

    alpha = round(alpha + 0.1, 1)
    beta = round(beta - 0.1, 1)

cv.destroyAllWindows()
