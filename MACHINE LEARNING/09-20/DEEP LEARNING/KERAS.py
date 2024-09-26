import tensorflow as tf
from tensorflow import Sequential
from tensorflow import Dense

model = Sequential()
model.add(Dense(64, activation='relu', input_dim=100))
model.add(Dense(10, activation='softmax'))

print(tf.__version__)

