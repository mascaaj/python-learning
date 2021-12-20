import cv2
import time

cap = cv2.VideoCapture('../../data/finger_move.mp4')

if not cap.isOpened():
    print('ERROR, FILE NOT FOUND')


def draw_rectangle(event, x, y, flags, param):
    global pt1, pt2, topleft_clicked, bottomright_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # reset the canvas
        if topleft_clicked and bottomright_clicked:
            pt1, pt2 = (0, 0), (0, 0)
            topleft_clicked = False
            bottomright_clicked = False
        if not topleft_clicked:
            pt1 = (x, y)
            topleft_clicked = True
        elif not bottomright_clicked:
            pt2 = (x, y)
            bottomright_clicked = True


# global variables
pt1, pt2 = (0, 0), (0, 0)
topleft_clicked = False
bottomright_clicked = False

# Connects name to image window
cv2.namedWindow('canvas')
# Connects callback to image window
cv2.setMouseCallback('canvas', draw_rectangle)

while True:
    ret, frame = cap.read()

    if ret:
        time.sleep(1 / 20)
        if topleft_clicked:
            cv2.circle(frame, center=pt1, radius=2, color=(0, 0, 255), thickness=1)
        if topleft_clicked and bottomright_clicked:
            cv2.rectangle(frame, pt1, pt2, color=(0, 0, 255), thickness=3)
        cv2.imshow('canvas', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
