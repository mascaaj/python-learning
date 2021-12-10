import numpy as np

mylist = [1, 2, 3]
print(type(mylist))

myarray = np.array(mylist)
print(type(myarray))

nd_array = np.arange(0, 10, 2)
print(nd_array)

zero_array = np.zeros(shape=(10, 5))
print(zero_array)

ones_array = np.ones(shape=(2, 4))
print(ones_array)

np.random.seed(101)
arr = np.random.randint(0, 100, 100)
print(arr)
print(arr.argmax())
print(arr.max())
print(arr.argmin())
print(arr.min())

arr2 = arr.reshape(10, 10)
print(arr2)
print(arr2.argmax())
print(arr2.max())
print(arr2.argmin())
print(arr2.min())

mat = np.arange(0, 100).reshape(10, 10)
print(mat)
print(mat[1, 9])

print(mat[:, 1])
tob = mat[1, :].reshape(10, 1)
print(tob)

mat[0:3, 0:4] = 0
print(mat)

mynewmat = mat.copy()
print(mynewmat)
