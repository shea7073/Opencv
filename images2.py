import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('00-puppy.jpg')

cv2.imshow("Puppy", img)
cv2.waitKey()

# If running outside pycharm
'''
while True:
    cv2.imshow("Puppy", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()
'''