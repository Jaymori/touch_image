import cv2
import os
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

        shrink = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        another = cv2.resize(shrink, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_AREA)

        cv2.imwrite(outway+a+'_low.jpg',another)

cv2.waitKey(0)
cv2.destroyAllWindows()
