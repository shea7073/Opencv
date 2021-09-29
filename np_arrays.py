import numpy as np

mylist = [1, 2, 3]

myarray = np.array(mylist)

# np.arange(0, 10, 2)

# np.zeros(shape=(5, 5))
# np.ones(shape=(2, 4))

np.random.seed(101)
arr = np.random.randint(0, 100, 10)
arr2 = np.random.randint(0, 100, 10)
# print(arr, arr2)

arr.argmax()  # returns location of max value
arr.argmin()  # returns index of min value
arr.mean()
# print(arr.reshape(2, 5))

mat = np.arange(0, 100).reshape(10, 10)
print(mat)

# print(mat[0, 9])

print(mat[0:4, 0:3])
newmat = mat.copy()

newmat[0:6, :] = 999
print(newmat)
