import cv2


img_color = cv2.imread("./data/image01.jpg", cv2.IMREAD_COLOR)

if img_color is None:
    print("이미지 파일을 읽을 수 없습니다.")
    exit(1)


cv2.namedWindow("Color")
cv2.imshow("Color", img_color)

cv2.waitKey(0)


img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

cv2.imshow("Grayscale", img_gray)

cv2.imwrite("./data/image01_gray.jpg", img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
