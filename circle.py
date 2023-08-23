import cv2
import numpy as np
#画像読み込み
img = cv2.imread(r"C:\Users\owner\CODE\circle.png", 0)

# 画像内から色の違う部分を探す
contours, hierarchy = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

#contoursには外側の枠まで入っている
#for i in range(0, len(contours) - 1):
#    img = cv2.drawContours(img, [contours[i]], 0, 192, 5)

count = 0
for cnt in contours:
    #外枠を排除するために原点(0,0)を含む配列は除外
    if [cnt][0][0][0][0] != 0 | [cnt][0][0][0][1] != 0:
        img = cv2.drawContours(img, [cnt], 0, 192, 5)
        count = count + 1

print("The number of circle is :", count)

cv2.imwrite(r"C:\Users\owner\CODE\circle-result.png", img)