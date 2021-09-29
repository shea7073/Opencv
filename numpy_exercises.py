import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

arr = np.ones(shape=(5, 5))
arr[:, :] = 10
# print(arr)

np.random.seed(101)
arr1 = np.random.randint(low=0, high=100, size=(5, 5))
print(arr1.max())
print(arr1.min())

pic = Image.open('00-puppy.jpg')
pic_arr = np.asarray(pic)
pic_blue = pic_arr.copy()
# plt.imshow(pic_arr)
pic_blue[:, :, 0] = 0
pic_blue[:, :, 1] = 0
plt.imshow(pic_blue)
plt.show()