import numpy as np
import cv2

# get all of the callback event in opencv
# events = [i for i in dir(cv2) if 'EVENT' in i]
"""
['EVENT_FLAG_ALTKEY',
 'EVENT_FLAG_CTRLKEY',
 'EVENT_FLAG_LBUTTON',
 'EVENT_FLAG_MBUTTON',
 'EVENT_FLAG_RBUTTON',
 'EVENT_FLAG_SHIFTKEY',
 'EVENT_LBUTTONDBLCLK',
 'EVENT_LBUTTONDOWN',
 'EVENT_LBUTTONUP',
 'EVENT_MBUTTONDBLCLK',
 'EVENT_MBUTTONDOWN',
 'EVENT_MBUTTONUP',
 'EVENT_MOUSEHWHEEL',
 'EVENT_MOUSEMOVE',
 'EVENT_MOUSEWHEEL',
 'EVENT_RBUTTONDBLCLK',
 'EVENT_RBUTTONDOWN',
 'EVENT_RBUTTONUP']

"""


# mouse callback function
def draw_circle(event, x, y, flags, param):
    # if the callback is left button click
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (0, 255, 0), -1)


flag = False


# draw any thing with mouse
def draw_with_mouse(event, x, y, flags, param):
    global flag
    if event == cv2.EVENT_LBUTTONDOWN:
        flag = True
        print('1', flag)
    elif event == cv2.EVENT_LBUTTONUP:
        flag = False
        print('2', flag)
    elif event == cv2.EVENT_MOUSEMOVE and flag:
        cv2.circle(img, (x, y), 1, (255, 0, 0))
        print('3', flag)
    else:
        pass


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow("image")
cv2.setMouseCallback("image", draw_with_mouse)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()