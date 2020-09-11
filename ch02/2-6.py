import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit(1)


while True:

    ret, img_frame = cap.read()

    if not ret:
        print("캡쳐 실패")
        break

    cv.imshow("Color", img_frame)

    key = cv.waitKey(1)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()
