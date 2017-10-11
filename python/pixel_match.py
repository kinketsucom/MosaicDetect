import cv2
import sys
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def npshow(npdata):
    b = npdata[:,:,0]
    g = npdata[:,:,1]
    r = npdata[:,:,2]
    merge_img = cv2.merge((r,g,b))
    img = Image.fromarray(merge_img)
    img.show()

def only_show(data):
    img = Image.fromarray(data)
    img.show()

def detecter(filename):
    image_path = "../files/"+filename+".jpeg"
    im = cv2.imread(image_path, 1) #読み込み BGR
    # npshow(im)
    # print(im)
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) #2値化
    # only_show(im_gray)
    # print(im_gray);
    # モザイク検出処理
    # ブロックで判定
    block_size = int(sys.argv[1])
    # threshold = 2
    counter = 0
    for i in range(0,im_gray.shape[1]-block_size,1):
        for j in range(0,im_gray.shape[0]-block_size,1):
            # 横の判定と縦の判定
            left_upper = int(im_gray[j][i])
            right_upper = int(im_gray[j][i+block_size-1])
            left_bottom = int(im_gray[j+block_size-1][i])
            right_bottom = int(im_gray[j+block_size-1][i+block_size-1])
            if(abs(left_upper-right_upper)==0 and abs(left_upper-left_bottom)==0 and abs(left_upper-right_bottom)==0):
                counter += 1

    print(filename+":"+str(counter))


def main():
    # detecter("data")
    # detecter("testdata3")
    # image_path = "../files/testdata3.jpeg"
    # image_path = "../files/data.jpeg"
    # im = cv2.imread(image_path, 1) #読み込み BGR
    # # npshow(im)
    # # print(im)
    # im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) #2値化
    # # only_show(im_gray)
    # print("*****")
    # # print(im_gray);
    # # モザイク検出処理
    # print("*****")
    #
    # # ブロックで判定
    # block_size = int(sys.argv[1])
    # counter = 0
    # print(im_gray.shape)
    # for i in range(0,im_gray.shape[1]-block_size,1):
    #     for j in range(0,im_gray.shape[0]-block_size,1):
    #         # 横の判定と縦の判定
    #         if(im_gray[j][i]==im_gray[j][i+block_size-1] and im_gray[j][i]==im_gray[j+block_size-1][i]):
    #             counter += 1
    #
    #
    #
    # print(counter)
    # for value in im_gray[0]:
    #     print(value)
    # x = np.random.normal(size = 100)
    # x = im_gray[0]
    # plt.hist(x,normed = True)
    # plt.title("Histgram")
    # plt.xlabel("x")
    # plt.ylabel("frequency")
    # plt.show()

if __name__ == '__main__':
    main()
