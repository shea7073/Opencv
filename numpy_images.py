import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

pic = Image.open('00-puppy.jpg')
pic_arr = np.asarray(pic)

# plt.imshow(pic_arr)

pic_red = pic_arr.copy()
# plt.imshow(pic_red[:, :, 0], cmap='gray')  # 0 refers to red
pic_red[:, :, 1] = 0
pic_red[:, :, 2] = 0
plt.imshow(pic_red)


plt.show()