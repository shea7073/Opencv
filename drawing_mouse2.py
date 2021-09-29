import cv2
import numpy as np
import matplotlib.pyplot as plt

drawing = False
ix, iy = -1, -1


def draw_rectangle(event, x, y, flags, params):

    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(img, (ix, iy), (x, y), color=(0, 255, 0), thickness=-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), color=(0, 255, 0), thickness=-1)


img = np.zeros(shape=(512, 512, 3))
cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing', draw_rectangle)


while True:

    cv2.imshow('my_drawing', img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()