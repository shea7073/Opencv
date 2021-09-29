import cv2
import numpy as np
import matplotlib.pyplot as plt


def load_img():

    blank_img = np.zeros((600, 600))
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(blank_img, text='ABCDE', org=(50, 300), fontFace=font, fontScale=5, color=(255, 255, 255), thickness=25, lineType=cv2.LINE_AA)
    return blank_img


def display_img(img):

    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')


kernel = np.ones((5, 5), dtype=np.uint8)
img = load_img()
# result = cv2.erode(img, kernel, iterations=4)  # Eroses away boundaries

'''
CREATES NOISE IN BACKGROUND AND USES FUNCTION TO REMOVE THAT NOISE
white_noise = np.random.randint(low=0, high=2, size=(600, 600))
white_noise = white_noise * 255
noise_img = white_noise + img
opening = cv2.morphologyEx(noise_img, cv2.MORPH_OPEN, kernel)
display_img(opening)
'''

'''
# CREATES BLACKNESS IN FOREGROUND AND THEN USES FUNCTION TO REDUCE NOISE
black_noise = np.random.randint(low=0, high=2, size=(600, 600))
black_noise = black_noise * -255
black_noise_img = img + black_noise
black_noise_img[black_noise_img == -255] = 0

closing = cv2.morphologyEx(black_noise_img, cv2.MORPH_CLOSE, kernel)
display_img(closing)
'''

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
display_img(gradient)

plt.show()
