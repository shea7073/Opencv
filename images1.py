import numpy as np
import matplotlib.pyplot as plt
import cv2


img = cv2.imread('00-puppy.jpg')
fixed = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(fixed)

# img_gray = cv2.imread('00-puppy.jpg', cv2.IMREAD_GRAYSCALE)

# plt.imshow(img_gray, cmap='gray')

# newest = cv2.resize(fixed, dsize=(1000, 400))
#plt.imshow(newest)

w_ratio = 0.5
h_ratio = 0.5

# newerer = cv2.resize(fixed, (0, 0), fixed, w_ratio, h_ratio)
# plt.imshow(newerer)

# new_img = cv2.flip(fixed, 0)  # (0, 1, -1)
# plt.imshow(new_img)

cv2.imwrite('new.jpg', fixed)

plt.show()
