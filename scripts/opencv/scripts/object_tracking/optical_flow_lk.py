import cv2
import numpy as np


# good features to track parameters
corner_track_params = dict(maxCorners=10, qualityLevel=0.3, minDistance=7, blockSize=7)
# speed v/s accuracy in metrics
lk_params = dict(winSize=(200, 200), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
cap = cv2.VideoCapture('../../data/hand_move.mp4')

if not cap.isOpened():
    print('ERROR, FILE NOT FOUND')

ret, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
prev_points = cv2.goodFeaturesToTrack(prev_gray, mask=None, **corner_track_params)

# Mask to draw on
mask = np.zeros_like(prev_frame)

while True:
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    next_pts, status, err = cv2.calcOpticalFlowPyrLK(prev_gray, frame_gray, prev_points, None, **lk_params)

    good_new = next_pts[status == 1]
    good_prev = prev_points[status == 1]

    for i, (new, prev) in enumerate(zip(good_new, good_prev)):
        x_new, y_new = new.ravel()
        x_prev, y_prev = prev.ravel()
        mask = cv2.line(img=mask, pt1=(int(x_new), int(y_new)),
                        pt2=(int(x_prev), int(y_prev)),
                        color=(0, 255, 0), thickness=3)
        frame = cv2.circle(frame, (int(x_new), int(y_new)), 8, (0, 0, 255), -1)
    img = cv2.add(frame, mask)
    cv2.imshow('tracking', img)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

    prev_gray = frame_gray.copy()
    prev_points = good_new.reshape(-1, 1, 2)

cap.release()
cv2.destroyAllWindows()
