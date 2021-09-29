import cv2
import numpy as np
import matplotlib.pyplot as plt


def load_img():

    img = cv2.imread('bricks.jpg').astype(np.float32) / 255
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


def display_img(img):

    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(img)

'''
gamma = 1/4  # less than 1 is lighter, more than 1 is darker
i = load_img()
result = np.power(i, gamma)
display_img(result)
'''

'''
BLURRING
kernel = np.ones(shape=(5, 5), dtype=np.float32)/25

img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text='bricks', org=(10, 600), fontFace=font, fontScale=10, color=(255, 0, 0), thickness=4)
dest = cv2.filter2D(img, -1, kernel)

display_img(dest)
'''

'''
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text='bricks', org=(10, 600), fontFace=font, fontScale=10, color=(255, 0, 0), thickness=4)
blurred = cv2.blur(img, ksize=(10, 10))
display_img(blurred)
'''

img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, text='bricks', org=(10, 600), fontFace=font, fontScale=10, color=(255, 0, 0), thickness=4)
# blur = cv2.GaussianBlur(img, ksize=(5, 5), sigmaX=10)
# blur = cv2.medianBlur(img, 5)
blur = cv2.bilateralFilter(img, 9, 75, 75)
display_img(blur)

plt.show()