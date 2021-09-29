import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('dog_backpack.jpg')
# fixed = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def draw_circle(event, x, y, flags, param):

    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 100, (0, 0, 255), thickness=10)


cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing', draw_circle)

while True:

    cv2.imshow('my_drawing', img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()