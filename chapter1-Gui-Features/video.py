import cv2

# capture video from camera
# 1st step, we need to create a VideoCapture object
cap = cv2.VideoCapture(0)       # parameter could be camera index or video file
while True:
    # ret represents if we successfully get a frame
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    # cv2.waitKey returns a 32bit interger, 0xFF sets left 24 bit to 0, because returns between(0, 255)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# playing video from file
cap = cv2.VideoCapture('test.avi')
while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()