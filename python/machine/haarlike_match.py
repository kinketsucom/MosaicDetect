# -*- coding: utf-8 -*-
# 画像からカスケード分類器を用いて顔認識を行うサンプル

##how to use
# python image.py 拡張子抜きファイル名
# [hoge.jpg]というファイルがあればhogeのこと
# このプログラムはjpgしか読み込まないと仮定している
import cv2
import sys

# サンプル顔認識特徴量ファイル
# cascade_path = "/usr/local/Cellar/opencv/3.3.0_3/share/OpenCV/haarcascades/haarcascade_eye.xml"
cascade_path = "/Users/admin/Documents/image_mosaic/python/machine/cascade/trained_data/cascade.xml"
args = sys.argv
image_path = str(args[1])
print(image_path)
# BGRで枠の色
color = (0, 0, 255) #白

# 画像の読み込み
image = cv2.imread(image_path)
# グレースケール変換
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 分類器を作る?みたいな作業
cascade = cv2.CascadeClassifier(cascade_path)

# 顔認識の実行
facerect = cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=1, minSize=(1, 1),maxSize=(300,300))
if len(facerect) > 0:
  # 検出した顔を囲む矩形の作成
  for rect in facerect:
    cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)
else:
  print("no Mosaic")

# 認識結果の表示
cv2.imshow("detected.jpg", image)

# 何かキーが押されたら終了
while(1):
  if cv2.waitKey(10) > 0:
    break
