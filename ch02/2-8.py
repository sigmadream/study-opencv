import cv2 as cv


cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit(1)


ret, img_frame = cap.read()

if not ret:
    print("캡쳐 실패")
    exit(1)


codec = cv.VideoWriter_fourcc("M", "J", "P", "G")
fps = 30.0
h, w = img_frame.shape[:2]

writer = cv.VideoWriter("./data/output.avi", codec, fps, (w, h))

if not writer.isOpened():
    print("동영상 파일을 준비할 수 없습니다.")
    exit(1)


while True:

    ret, img_frame = cap.read()

    if not ret:
        print("캡쳐 실패")
        break

    writer.write(img_frame)

    cv.imshow("Color", img_frame)

    key = cv.waitKey(1)
    if key == 27:
        break

cap.release()
writer.release()
cv.destroyAllWindows()
