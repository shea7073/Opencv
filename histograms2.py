import cv2
import numpy as np
import matplotlib.pyplot as plt


rainbow = cv2.imread('rainbow.jpg')
show_rainbow = cv2.cvtColor(rainbow, cv2.COLOR_BGR2RGB)

img = rainbow

mask = np.zeros(img.shape[:2], np.uint8)
mask[300:400, 100:400] = 255

masked_img = cv2.bitwise_and(img, img, mask=mask)
show_masked_img = cv2.bitwise_and(show_rainbow, show_rainbow, mask=mask)

# plt.imshow(show_masked_img)
hist_mask_values_red = cv2.calcHist([rainbow], channels=[2], mask=mask, histSize=[256], ranges=[0, 256])
# plt.plot(hist_mask_values_red)


plt.show()