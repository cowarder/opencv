import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((512, 512, 3), np.uint8)

# draw line
cv2.line(img, (0, 0), (500, 500), (0, 255, 0), 1)           # the last parameter is line width

# draw rectangular
cv2.rectangle(img, (300, 0), (400, 100), (0, 0, 255), 2)    # (x, y), top left and bottom right

# draw circle
cv2.circle(img, (350, 50), 50, (255, 0, 0), -1)

# draw ellipse
cv2.ellipse(img, (256, 256), (50, 100), 10, 0, 180, (255, 0, 0), -1)

# draw polygon
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))                               # vertices must be rows*1*2
cv2.polylines(img, [pts], True, (0, 255, 255))

# put text
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, "NB", (10, 400), font, 4, (255, 255, 255), 3, cv2.LINE_AA)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()