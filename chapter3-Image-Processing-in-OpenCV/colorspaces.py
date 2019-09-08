import cv2
import numpy as np

"""
    Goal:
        In this chapter, you will learn how to convert images from color space, like BGR->RGB, BGR->HSV
        
    Func:
        cv2.cvtColor(), cv2.inRange()
"""

# we use cv2.cvtColr() to convert color space, cv2.cvtColor(img, flag), flag controls the convert method
# show flag parameters
print([x for x in dir(cv2) if x.startswith('COLOR_')])

# BGR->gray
img = cv2.imread('../pics/lenna.jpeg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# BGR->HSV
HSV_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

print("start tracking")
# object tracking
cap = cv2.VideoCapture(0)
while True:
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([100,50,50])
    upper_blue = np.array([124,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask= mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
