import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


def generate_data(num_samples):
    X = np.random.randint(0, 100, (num_samples, 4))
    y = np.sum(X, axis=1) 
    return X, y

X, y = generate_data(10000)

model = keras.Sequential([
    layers.Input(shape=(4,)),
    layers.Dense(10, activation='relu'),
    layers.Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(X, y, epochs=100, batch_size=32)

model.save('sumator.h5')

test_input = np.array([[10, 20, 30, 3], [5, 15, 25, 8]])
predictions = model.predict(test_input)

for i, input_numbers in enumerate(test_input):
    print(f"The sum of {input_numbers} is predicted to be {predictions[i][0]:.2f}")
