import cv2
import numpy as np
import matplotlib.pyplot as plt


# read image
img = cv2.imread("../pics/lenna.jpeg", flags=1)     # flags 0:gray mode flags 1:RGB mode, default:1
print(type(img))
# print(np.asarray(img).shape)                      # (H, W, C)

# display image
# by default window would suit image automatically, adding this line, we can resize image
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow("image", img)                            # the first parameter is window name

# destroy windows
cv2.waitKey(0)                                      # if 0, press any key to terminate, else means milliseconds
cv2.destroyAllWindows()                             # or cv2.destroyWindow('image')

# write image
# cv2.imwrite("../pics/lenna(gray).png", img)

# or we can get the specific default key, and regard it as a condition
# if we press 'ESC', destroy all windows and exit, if we press 's', we would save and exit
#     k = cv2.waitKey(0)
#     if k == 27:
#         cv2.destroyAllWindows()
#     elif k == ord('s'):
#         cv2.imwrite("../pics/lenna(copy).png", img)
#         cv2.destroyAllWindows()

# using matplotlib to show image
# waring: opencv colorful image format is (BGR), if we want to show image with matplotlib
# we need to transfer it into RGB format
b, g, r = cv2.split(img)
img = cv2.merge([r, g, b])                          # or we transfer into numpy method: img = img[:, :, (2, 1, 0)]
plt.imshow(img)
plt.show()
