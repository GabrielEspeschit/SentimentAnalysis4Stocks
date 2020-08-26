import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow import keras
from sklearn.model_selection import train_test_split

df = pd.read_pickle('Dados/Dados_modelo.plk')

X = df.media.apply(np.squeeze, axis=0)
X = pd.DataFrame(X.values.tolist(), index=X.index).to_numpy()
y = pd.DataFrame(df.classificador).apply(np.squeeze, axis=0).to_numpy()

X_train, X_test, y_train_orig, y_test_orig = train_test_split(X, y, test_size = 0.05)

y_train = np.reshape(y_train_orig, y_train_orig.shape[0]).astype('uint8')
y_test = np.reshape(y_test_orig, y_test_orig.shape[0]).astype('uint8')

class_names = ['Muito Ruim', 'Ruim', 'Normal', 'Bom', 'Muito Bom']

print ("number of training examples = " + str(X_train.shape[0]))
print ("number of test examples = " + str(X_test.shape[0]))
print ("X_train shape: " + str(X_train.shape))
print ("y_train shape: " + str(y_train.shape))
print ("X_test shape: " + str(X_test.shape))
print ("y_test shape: " + str(y_test.shape))

model = keras.Sequential([
    keras.layers.InputLayer(input_shape=(100,)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(5, activation='softmax')
])

opt = keras.optimizers.Adam(learning_rate=0.01)
model.compile(optimizer=opt, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10, batch_size=12)