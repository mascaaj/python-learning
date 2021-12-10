import cv2
import numpy as np


ix, iy = -1, -1
drawing = False


# callbacks
def draw_circle(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (0, 255, 0), -1)


def draw_square(event, x, y, flags, param):
    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        # log mouse click event as drawing
        drawing = True
        # push clicked xy to global params
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            # begin drawing, update x,y based on mouse position
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        # stop drawing, redraw final rectangle
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)


# Connects name to image window
cv2.namedWindow('canvas')
# Connects callback to image window
cv2.setMouseCallback('canvas', draw_square)
# display image
img = np.zeros((512, 512, 3), np.int8)


while True:
    cv2.imshow('canvas', img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
