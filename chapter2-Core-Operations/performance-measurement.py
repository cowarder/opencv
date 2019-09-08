import cv2
import numpy as np

e1 = cv2.getTickCount()
img = cv2.imread(",,/pics/lenna.jpeg")
for i in range(5, 49, 2):
    img = cv2.medianBlur(img, 49)
e2 = cv2.getTickCount()
t = (e2 - e1) / cv2.getTickFrequency()
print(t)                                        # get running time of code


# check if code is optimized
print(cv2.useOptimized())

cv2.setUseOptimized(False)                      # no optimization

