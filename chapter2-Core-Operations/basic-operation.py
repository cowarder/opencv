import numpy as np
import cv2

# get and modify rgb value in spesific pixel
img = cv2.imread('../pics/lenna.jpeg')
print(img.dtype)
print(img.shape)

print(img[100, 100])                            # [80 109 190]
img[100, 100] = [0, 0, 0]

# better(faster) access and modify pixel value method, numpy array method
print(img.item(100, 101, 1))                    # the last parameter represents b or g or r
img.itemset((100, 100, 2), 100)
print(img.item(100, 100, 2))

# channel split and merge
# split() is a very time_consuming method, b = img[:, :, 0] is better
b, g, r = cv2.split(img)

img = cv2.merge((b, g, r))                      # transfer channel img = img[:, :, (2, 1, 0)]

