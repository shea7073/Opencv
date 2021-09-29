import cv2
import numpy as np
import matplotlib.pyplot as plt

# gorilla = cv2.imread('gorilla.jpg', 0)


def display(img, cmap=None):

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap)


# display(gorilla, cmap='gray')

# hist_values = cv2.calcHist([gorilla], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
# plt.plot(hist_values)

# eq_gorilla = cv2.equalizeHist(gorilla)
# display(eq_gorilla, cmap='gray')

# hist_values = cv2.calcHist([eq_gorilla], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
# plt.plot(hist_values)

gorilla = cv2.imread('gorilla.jpg')
show_gorilla = cv2.cvtColor(gorilla, cv2.COLOR_BGR2RGB)

hsv = cv2.cvtColor(gorilla, cv2.COLOR_BGR2HSV)

hsv[:, :, 2] = cv2.equalizeHist(hsv[:, :, 2])

eq_color_gorilla = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)

display(eq_color_gorilla)

plt.show()
