import cv2

#画像の読み込み
img = cv2.imread('C:/Users/owner/CODE/strawberry.jpg')

#画像の表示
cv2.imshow('sample', img)
cv2.waitKey(0)
