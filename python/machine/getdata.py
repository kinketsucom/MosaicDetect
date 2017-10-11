import cv2
import sys
import os
import re

if __name__ == "__main__":
    dir = os.getcwd()# カレントディレクトリのパスを取得
    # print(dir+"/pos")
    files = os.listdir(dir+"/pos")# ファイルのリストを取得
    count = 0# カウンタの初期化
    for file in files:# ファイルの数だけループ
        index = re.search('.png', file)# 拡張子がpngのものを検出
        if index:# jpgの時だけ（今回の場合は）カウンタをカウントアップ
            count = count + 1

    # print(count)# ファイル数の表示

    f = open('positive.dat','w')
    for i in range(1,count+1):
        img = cv2.imread(dir+"/pos/"+str(i)+".png", cv2.IMREAD_UNCHANGED)

        # 画像ファイルの読み込みに失敗したらエラー終了
        if img is None:
            print(i)
            print("Failed to load image file.")
            sys.exit(1)

        # カラーとグレースケールで場合分け
        if len(img.shape) == 3:
            height, width, channels = img.shape[:3]
        else:
            height, width = img.shape[:2]
            channels = 1

        # 取得結果（幅，高さ)
        f.write("./pos/"+str(i)+".png 1 0 0 "+str(width)+" "+str(height)+"\n")

    f.close
