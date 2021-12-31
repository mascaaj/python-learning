import cv2
import numpy as np


cap = cv2.VideoCapture('../../data/hand_move.mp4')

if not cap.isOpened():
    print('ERROR, FILE NOT FOUND')

ret, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

# Mask to draw on
mask = np.zeros_like(prev_frame)
# max out saturation
mask[:, :, 1] = 255

while True:
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    flow = cv2.calcOpticalFlowFarneback(prev_gray, frame_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    mag, angle = cv2.cartToPolar(flow[:, :, 0], flow[:, :, 1], angleInDegrees=True)
    # Calculate hue as half angle
    mask[:, :, 0] = angle / 2
    # Calculate value as magnitude between 0-255 normalized
    mask[:, :, 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
    bgr = cv2.cvtColor(mask, cv2.COLOR_HSV2BGR)
    cv2.imshow('tracking', bgr)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

    prev_gray = frame_gray.copy()

cap.release()
cv2.destroyAllWindows()
