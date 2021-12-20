import cv2
import time

cap = cv2.VideoCapture('../../data/finger_move.mp4')

if not cap.isOpened():
    print('ERROR, FILE NOT FOUND')

height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

x = width // 2
y = height // 2
w = width // 4
h = height // 4

while True:
    ret, frame = cap.read()

    if ret:
        time.sleep(1 / 20)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=4)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
