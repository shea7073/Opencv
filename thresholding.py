import cv2
import matplotlib.pyplot as plt
import numpy as np

# img = cv2.imread('rainbow.jpg', 0)

# ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)  # INV or no INV
# ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC) # INV or no INV
# ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)  # INV or no INV


def show_pic(img):
    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')


img = cv2.imread('crossword.jpg', 0)

ret, th1 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)

th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)
# PLAY WITH DIFFERENT ADAPTIVE THRESHOLD ARGUMENTS

blended = cv2.addWeighted(src1=th1, alpha=.6, src2=th2, beta=0.4, gamma=0)

show_pic(blended)

#plt.imshow(img, cmap='gray')

plt.show()