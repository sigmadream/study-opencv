import cv2
import numpy as np

# 전처리
# 1. 이미지 읽기
img = cv2.imread("./data/coins_connected.jpg")
rows, cols = img.shape[:2]

# 2. 표면을 흐릿하게 피라미드평균시프트 적용
mean = cv2.pyrMeanShiftFiltering(img, 20, 50)

# 3. 바이너리 이미지 변환
gray = cv2.cvtColor(mean, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 4. 거리 변환 => 거리 값을 0 ~255로 변환
dst = cv2.distanceTransform(thresh, cv2.DIST_L2, 3)
dst = (dst / (dst.max() - dst.min()) * 255).astype(np.uint8)

# 5. 거리 변환결과에서 로칼 최대 값 구하기
## 팽창 적용(동전 크기 정도의 구조화 요소 필요),
localMx = cv2.dilate(dst, np.ones((50, 50), np.uint8))
## 로칼 최대 값 저장 할 배열 생성
lm = np.zeros((rows, cols), np.uint8)
## 팽창 적용전 이미지와 같은 픽셀이 로컬 최대 값이므로 255로 설정
lm[(localMx == dst) & (dst != 0)] = 255

# 6. 로컬 최대값으로 색 채우기
## 로컬 최대 값이 있는 좌표 구하기
seeds = np.where(lm == 255)
seed = np.stack((seeds[1], seeds[0]), axis=-1)
## 색 채우기를 위한 채우기 마스크 생성
fill_mask = np.zeros((rows + 2, cols + 2), np.uint8)
for x, y in seed:
    ## 로칼 최대값을 시드로해서 평균 시프트 영상에 색채우기
    ret = cv2.floodFill(
        mean, fill_mask, (x, y), (255, 255, 255), (10, 10, 10), (10, 10, 10)
    )

# 7. 색 채우기 적용한 영상에 다시 거리 변환 적용
gray = cv2.cvtColor(mean, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
dst = cv2.distanceTransform(thresh, cv2.DIST_L2, 5)
dst = ((dst / (dst.max() - dst.min())) * 255).astype(np.uint8)

# 8. 거리 변환 결과값의 절반 이상을 차지한 영역은 확실한 전경으로 설정
ret, sure_fg = cv2.threshold(dst, 0.5 * dst.max(), 255, 0)

# 9. 거리 변환 결과를 반전해서 확실한 배경 찾기
_, bg_th = cv2.threshold(dst, 0.3 * dst.max(), 255, cv2.THRESH_BINARY_INV)
bg_dst = cv2.distanceTransform(bg_th, cv2.DIST_L2, 5)
bg_dst = ((bg_dst / (bg_dst.max() - bg_dst.min())) * 255).astype(np.uint8)
ret, sure_bg = cv2.threshold(bg_dst, 0.3 * bg_dst.max(), 255, cv2.THRESH_BINARY)

# 10. 불확실한 영역 설정 : 확실한 배경을 반전해서 확실한 전경을 빼기
ret, inv_sure_bg = cv2.threshold(sure_bg, 127, 255, cv2.THRESH_BINARY_INV)
unkown = cv2.subtract(inv_sure_bg, sure_fg)

# 11. 연결된 요소 레이블링
_, markers = cv2.connectedComponents(sure_fg)

# 12. 레이블링을 1씩 증가 시키고 0번 레이블 알 수 없는 영역을 0번 레이블로 설정
markers = markers + 1
markers[unkown == 255] = 0
colors = []
marker_show = np.zeros_like(img)
for mid in np.unique(markers):
    color = [int(j) for j in np.random.randint(0, 255, 3)]
    colors.append((mid, color))
    marker_show[markers == mid] = color
    coords = np.where(markers == mid)
    x, y = coords[1][0], coords[0][0]
    cv2.putText(
        marker_show,
        str(mid),
        (x + 20, y + 20),
        cv2.FONT_HERSHEY_PLAIN,
        2,
        (255, 255, 255),
    )

# 13. 레이블링이 완성된 마커로 워터 쉐드 적용
markers = cv2.watershed(img, markers)

for mid, color in colors:
    marker_show[markers == mid] = color
    coords = np.where(markers == mid)
    if coords[0].size <= 0:
        continue
    x, y = coords[1][0], coords[0][0]
    cv2.putText(
        marker_show,
        str(mid),
        (x + 20, y + 20),
        cv2.FONT_HERSHEY_PLAIN,
        2,
        (255, 255, 255),
    )
marker_show[markers == -1] = (0, 255, 0)

img[markers == -1] = (0, 255, 0)

# 14. 동전 추출을 위한 마스킹 생성
mask = np.zeros((rows, cols), np.uint8)

# 15. 배경 마스크 생성
mask[markers != 1] = 255

# 16. 배경 지우기
nobg = cv2.bitwise_and(img, img, mask=mask)

# 17. 동전만 있는 라벨 생성 (배경(1), 경계(-1) 없는)
coin_label = [l for l in np.unique(markers) if (l != 1 and l != -1)]

# 18. 동전 라벨 순회 하면서 동전 영역만 추출
for i, label in enumerate(coin_label):
    mask[:, :] = 0
    mask[markers == label] = 255
    coins = cv2.bitwise_and(img, img, mask=mask)
    contour, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # 동전을 감싸는 사각형 좌표
    x, y, w, h = cv2.boundingRect(contour[0])
    # 동전 영역만 추출해서 출력
    coin = coins[y : y + h, x : x + w]
    cv2.imwrite("./data/coin/coin%d.jpg" % (i + 1), coin)
cv2.waitKey()
cv2.destroyAllWindows()
