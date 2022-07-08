
# Using tensorflow

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("mnist/", one_hot=True)
mnist.train.images



# Using Keras

from keras.datasets import mnist

# READ MNIST data
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Check inside
len(X_train) # 60000
len(X_test)  # 10000

print(X_train[0])
print(X_train[0].shape) # 28x28 pixels
print(y_train) # labels

a = X_train[0]
a.shape

b = a.reshape(784)
b.shape


# Plot it
from matplotlib import pyplot as plt
plt.imshow(X_train[0], interpolation='nearest')
plt.gray()