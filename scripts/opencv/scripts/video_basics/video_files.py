import cv2
import time

cap = cv2.VideoCapture('../../data/finger_move.mp4')

if not cap.isOpened():
    print('ERROR, FILE NOT FOUND')

while True:
    ret, frame = cap.read()

    if ret:
        time.sleep(1 / 20)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
