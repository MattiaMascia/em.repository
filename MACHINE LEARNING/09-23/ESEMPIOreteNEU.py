import os
import warnings

# Imposta il livello di log di TensorFlow per sopprimere i messaggi INFO e WARNING
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 0 = Tutti i log, 1 = INFO, 2 = WARNING, 3 = ERROR

# Disabilita specifici avvisi di Keras
warnings.filterwarnings('ignore', category=UserWarning, module='keras.layers.core.dense')

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, classification_report

# Caricamento del dataset MNIST
(X_train, y_train), (X_test, y_test) = mnist.load_data()
#X_train, X_test contengono le immagini; y_train, y_test contengono le etichette.

# Pre-elaborazione dei dati
X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255
#i valori vengono normalizzati tra 0 e 1, rendendo il training del modello più efficiente

X_train = X_train.reshape(-1, 28*28)
X_test = X_test.reshape(-1, 28*28)
#appiattisco i dati in un vettore

y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)
#vengono convertite in formato one-hot, in modo che ogni cifra sia rappresentata come un vettore con 10 elementi

# Creazione del modello
model = Sequential()
model.add(Dense(units=128, activation='relu', input_shape=(784,)))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

#Il primo strato denso (Dense) ha 128 neuroni, funzione di attivazione ReLU 
# e riceve input di 784 valori (ogni immagine appiattita).

#Il secondo strato ha 64 neuroni e utilizza anche la funzione ReLU.

#L'ultimo strato ha 10 neuroni (uno per ogni possibile cifra) 
# e usa softmax per la classificazione multi-classe

# Compilazione del modello
model.compile(optimizer='adam',#per minimizzare la funzione di perdita
              loss='categorical_crossentropy',#viene utilizzata per problemi di classificazione multi-classe
              metrics=['accuracy'])#misuro l'accuratezza durante la compilazione


# Addestramento del modello
history = model.fit(X_train, y_train,
                    epochs=10,
                    batch_size=32,
                    validation_split=0.1)
#Il modello viene addestrato per 10 epoche, con una dimensione del batch di 32 immagin

# Valutazione del modello
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f'Perdita sul test set: {test_loss:.4f}')
print(f'Accuratezza sul test set: {test_accuracy:.4f}')

# Predizioni
predictions = model.predict(X_test)
predicted_classes = np.argmax(predictions, axis=1)
true_classes = np.argmax(y_test, axis=1)
#predict_classis: Estrae la classe prevista da softmax.
#true_classes: Estrae la classe vera dal set di test.

# Matrice di confusione
conf_matrix = confusion_matrix(true_classes, predicted_classes)
plt.figure(figsize=(10,8))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.title('Matrice di Confusione')
plt.xlabel('Classe Predetta')
plt.ylabel('Classe Vera')
plt.show()

# Report di classificazione
report = classification_report(true_classes, predicted_classes)
print('Report di Classificazione:')
print(report)

# Visualizzazione di alcune predizioni
num_images = 5
random_indices = np.random.choice(len(X_test), num_images)
plt.figure(figsize=(15,3))
for i, idx in enumerate(random_indices):
    image = X_test[idx].reshape(28, 28)
    true_label = true_classes[idx]
    predicted_label = predicted_classes[idx]
    
    plt.subplot(1, num_images, i+1)
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.title(f'T:{true_label}, P:{predicted_label}')
plt.show()

#Vengono scelte 5 immagini casuali dal test set e visualizzate
# T è la vera etichetta, e P è la classe predetta dal modello
