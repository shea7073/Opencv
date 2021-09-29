import cv2
import numpy as np
import matplotlib.pyplot as plt


def display_img(img, cmap=None):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap)


img = cv2.imread('giraffes.jpg')
# img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# display_img(th1, cmap='gray')

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

display_img(img_hsv)

plt.show()