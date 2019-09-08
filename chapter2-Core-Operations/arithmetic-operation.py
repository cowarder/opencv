import cv2
import numpy as np

# we can add two image like cv2.add(img1, img2)
x = np.uint8([250])
y = np.uint8([10])
print(cv2.add(x, y))                                # [[255]]  cv2 is saturated
print(x + y)                                        # [4] numpy would get mod

# image blending
# images are added in the form: g(x) = (1-alpha) * f1(x) + alpha * f2(x)

img1 = cv2.imread('../pics/forest.jpeg', 1)
img2 = cv2.imread('../pics/lenna.jpeg', 1)
w = int(img1.shape[1])
h = int(img1.shape[0])
dim = (w, h)


"""
    interpolations:
    1.cv.INTER_NEAREST:
    2.cv2.INTER_LINEAR: 
    3.cv2.INTER_CUBIC: 
    4.cv2.INTER_AREA:
"""
img2 = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA)

print(img1.shape)
print(img2.shape)

dst = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()