from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import Adam
from keras.utils import np_utils

# Read data
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# data reshape and change the range of pixel
X_train = X_train.reshape(60000, 784).astype('float32')
X_test  = X_test.reshape(10000, 784).astype('float32')
X_train /= 255 # change the range of pixel data (pixel range: 0 (black) to 255 (white)
X_test  /= 255


# change label form from int number to array
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)


# Define model
model = Sequential()
model.add(Dense(512, input_shape=(784,))) #input dimension = 784, and first hidden layer has 512 nodes
model.add(Activation('relu'))
model.add(Dropout(0.2)) # remove 20% of nodes in order to prevent over-fitting

model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.2))

model.add(Dense(10)) # why 10? Because we have 10 classes
model.add(Activation('softmax')) # softmax is a classic choice for a classification task

# building model
model.compile(
    loss='categorical_crossentropy', # loss function: https://keras.io/losses/
    optimizer=Adam(),# One of the gradient methods which outperforms other optimizer
    metrics=['accuracy'])


# train the model
hist = model.fit(X_train, y_train)

# evaluate the model
score = model.evaluate(X_test, y_test, verbose=1) #verbose 1: print the process (0, do not print)
print('loss=', score[0])
print('accuracy=', score[1])


