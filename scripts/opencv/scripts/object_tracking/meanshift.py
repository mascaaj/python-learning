"""
Mean Shift
Cannot test this, no webcam, will need to revisit
"""
import cv2

cap = cv2.VideoCapture('../../data/video_capture.mp4')

if not cap.isOpened():
    print('ERROR, FILE NOT FOUND')

ret, frame = cap.read()
# prev_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

face_classifier = cv2.CascadeClassifier('../../data/haarcascades/haarcascade_frontalface_default.xml')

faces = face_classifier.detectMultiScale(frame)
(face_x, face_y, w, h) = tuple(faces[0])
track_window = (face_x, face_y, w, h)

roi = frame[face_y:face_y + h, face_x:face_x + w]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

roi_hist = cv2.calcHist(hsv_roi, [0], None, [180], [0, 180])

cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
    ret, track_window = cv2.meanShift(dst, track_window, term_crit)
    x, y, w, h = track_window
    img2 = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)

    cv2.imshow('tracking', img2)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
