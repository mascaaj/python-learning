import cv2


# default camera capture
cap = cv2.VideoCapture(0)

width = int(cap.get(cap.CAP_PROP_FRAME_WIDTH))  # floating point
height = int(cap.get(cap.CAP_PROP_FRAME_HEIGHT))

# Codec selection here is important, different for different os'
writer = cv2.VideoWriter('~/Downloads/test.mp4', cv2.VideoWriter_fourcc(*'XVID'), 20, (width, height))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)

    writer.write(gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
