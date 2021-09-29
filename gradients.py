import cv2
import numpy as np
import matplotlib.pyplot as plt


def display_img(img):

    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')


img = cv2.imread('sudoku.jpg', 0)

# sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
# sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

laplcian = cv2.Laplacian(img, cv2.CV_64F)

display_img(laplcian)

plt.show()
