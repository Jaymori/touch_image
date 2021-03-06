import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

#way는 이미지가 있는 폴더
#outway는 배출할 폴더

way='./img/'
outway='./afimg/'

for root, dirs, files in os.walk(way):
    for file in files:
        a=os.path.splitext(file)[0]
        b=os.path.splitext(file)[1]
        #jpg일 경우만
        if(b!='.jpg') : continue
        img = cv2.imread(way+file)
        height, width = img.shape[:2]

        new_image = np.zeros(img.shape, img.dtype)
        alpha = 0.7
        beta = 0

        for y in range(img.shape[0]):
            for x in range(img.shape[1]):
                for c in range(img.shape[2]):
                    new_image[y, x, c] = np.clip(alpha * img[y, x, c] + beta, 0, 255)

        cv2.imwrite(outway+a+'_dark.jpg',new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
