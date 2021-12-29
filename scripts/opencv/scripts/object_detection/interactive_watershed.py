import numpy as np
import cv2
from matplotlib import cm


# Read in image, make a copy
road = cv2.imread('../../data/road_image.jpg')
road_copy = road.copy()

# create marker image and segment image based on original image shape
marker_image = np.zeros(road.shape[:2], dtype=np.int32)
segments = np.zeros(road.shape, dtype=np.int8)


# import color pallet for segments and interactive markers
# get as numpy array and normalize to 255
# need output as tuple of rgb
def create_rgb(i):
    return tuple(np.array(cm.tab10(i)[:3]) * 255)


# create colors output array
colors = []
for i in range(10):
    colors.append(create_rgb(i))

# MOUSE CALLBACK

# variables
total_markers = 10
current_marker = 1
# Checks if markers have been updated by watershed
marks_updated = False


# functions
def mouse_callback(event, x, y, flags, params):
    global marks_updated
    if event == cv2.EVENT_LBUTTONDOWN:
        # for watershed algo
        cv2.circle(marker_image, (x, y), 10, current_marker, -1)
        # For user to view
        cv2.circle(road_copy, (x, y), 10, colors[current_marker], -1)
        # inform somebody that new mark exists, flag
        marks_updated = True


cv2.namedWindow('Road Image')
cv2.setMouseCallback('Road Image', mouse_callback)

while True:

    # SHow the 2 windows
    cv2.imshow('WaterShed Segments', segments)
    cv2.imshow('Road Image', road_copy)

    # Close everything if Esc is pressed
    k = cv2.waitKey(1)

    if k == 27:
        break

    # Clear all colors and start over if 'c' is pressed
    elif k == ord('c'):
        road_copy = road.copy()
        marker_image = np.zeros(road.shape[:2], dtype=np.int32)
        segments = np.zeros(road.shape, dtype=np.int8)

    # Change the color based on number input
    # number to character, cast as integer
    elif k > 0 and chr(k).isdigit():
        current_marker = int(chr(k))

    if marks_updated:
        # copy the marker image
        marker_image_copy = marker_image.copy()
        # call watershed
        cv2.watershed(road, marker_image_copy)
        # reinitialize the segments image
        segments = np.zeros(road.shape, dtype=np.int8)
        # assign segments based on colors and segment number in marker image
        for color_index in range(total_markers):
            segments[marker_image_copy == color_index] = colors[color_index]

cv2.destroyAllWindows()
