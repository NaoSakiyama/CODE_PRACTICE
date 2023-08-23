import cv2
import numpy as np
import os

path1 = os.getcwd()
path2 = '.\CODE'
path3 = os.path.join(path1, path2)
print('path3)
os.chdir(path3)

#画像読み込み
img = cv2.imread('strawberry.jpg', 0)
img_org = cv2.imread('strawberry.jpg')
cv2.imshow("image", img)


#閾値
threshold =180
#閾値で二値化
ret, img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

#画像内から色の違う部分を探す
contours, hierarchy = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

count = 0
for cnt in contours:
    #小さなエリアは無視
    if cv2.contourArea(cnt) < 1500:
        continue
    
    #外枠を排除するために原点(0,0)を含む配列は除外
    if [cnt][0][0][0][0] != 0 | [cnt][0][0][0][1] != 0:
        img = cv2.drawContours(img_org, [cnt], 0, 255, 5)
        count = count + 1
        
    print("The number of strawberry is :", count)
    
    cv2.imwrite('strawberry-result.jpg', img)