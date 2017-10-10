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

def detecter(data):
    return 0


def main():
    image_path = "../files/testdata3.jpeg"
    im = cv2.imread(image_path, 1) #読み込み BGR
    # npshow(im)
    # print(im)
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) #2値化
    # only_show(im_gray)
    print("*****")
    # print(im_gray);
    # モザイク検出処理
    print("*****")
    print(im_gray[0][0])

    x = np.random.normal(size = 100)

    plt.hist(x)
    plt.title("Histgram")
    plt.xlabel("x")
    plt.ylabel("frequency")
    plt.show()

if __name__ == '__main__':
    main()
