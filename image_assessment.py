import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('dog_backpack.jpg')
fixed = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# new_img = cv2.flip(fixed, 0)

# cv2.rectangle(fixed, pt1=(200, 400), pt2=(600, 700), color=(255, 0, 0), thickness=10)

vertices = np.array([[100, 800], [400, 400], [700, 800]], dtype=np.int32)
points = vertices.reshape((-1, 1, 2))
cv2.fillPoly(fixed, [points], color=(0, 0, 255))

plt.imshow(fixed)

plt.show()