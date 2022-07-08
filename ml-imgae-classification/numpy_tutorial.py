# numpy docs: http://www.numpy.org
# It let us handle a multidimensional array object, and tools for working with these arrays.


import numpy as np

a = np.array([[1,2],[3,4]])
print(a)

a.shape

a.dtype

b = np.array([[3,6],[0,6]])

a + b

a * b

a[0][1]

a.reshape(4)

a = np.arange(6)
a = np.arange(6).reshape((3, 2))
a.dtype
a.reshape(2,3).astype('float32')


a = a * 3
print(a)

print(a.mean())

