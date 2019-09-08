import cv2
import numpy as np

"""
    Goal:
        learn to apply different geometric transformations like translation, rotation, affine transformation
        
    Func:
        cv2.getPerspectiveTransform
    
"""

# transformations: cv2.warpAffine cv2.warpPerspective

# scaling
img = cv2.imread('../pics/lenna.jpeg')
height, width = img.shape[:2]
res = cv2.resize(img, (int(2*width), int(2*height)), interpolation=cv2.INTER_CUBIC)
cv2.imshow('image', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

# translation
# shift the location of image, shift x, y in height and width relatively
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (width, height))
cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# rotation
