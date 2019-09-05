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
print(img1.size())
print(img2.size())

dst = cv2.addWeighted(img1, 0.3, img2, 0.7, 0)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()