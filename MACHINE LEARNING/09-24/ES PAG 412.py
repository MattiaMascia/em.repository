import os
import warnings

# Imposta il livello di log di TensorFlow per sopprimere i messaggi INFO e WARNING
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 0 = Tutti i log, 1 = INFO, 2 = WARNING, 3 = ERROR

# Disabilita specifici avvisi di Keras
warnings.filterwarnings('ignore', category=UserWarning, module='keras.layers.core.dense')

import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense, Input # type: ignore
from tensorflow.keras.datasets import mnist # type: ignore
import matplotlib.pyplot as plt

#1 carico il dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

#vedo un esempio
plt.imshow(X_train[0], cmap='gray')
plt.title(f'Etichetta: {y_train[0]}')
plt.show()

#normalizzo i dati
X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255

#faccio un reshape sulle  x per appiattire i dati
X_train = X_train.reshape(-1, 28*28)
X_test = X_test.reshape(-1, 28*28)

from tensorflow.keras.utils import to_categorical # type: ignore
#converto le y(etichette) e trasformo in categoria (ogni cifra viene rappresentata in un vettore tipo [0,0,0,1,0...])
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

from tensorflow.keras.models import Sequential # type: ignore
#2 Costruisco un modello sequenziale
model = Sequential()
# aggiungo gli strati
model.add(Dense(units=128, activation='relu', input_shape=(784,)))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

#3 Compilo il modello
model.compile(optimizer='adam', #utilizzo un optimizer
              loss='categorical_crossentropy', #viene utilizzata per problemi di classificazione multi-classe 
              metrics=['accuracy']) #Mostra l'accuratezza

#4 Addestro il modello  sui dati di training con uno split del 10%
history = model.fit(X_train, y_train,
                    epochs=10,
                    batch_size=32,
                    validation_split=0.1)

#5 Valuto le prestazioni del modello
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f'Perdita sul test set: {test_loss:.4f}')
print(f'Accuratezza sul test set: {test_accuracy:.4f}')


#Faccio predizioni sul modello Test Set

# Predizioni sul test set
predictions = model.predict(X_test)

# Conversione delle predizioni in etichette
predicted_classes = np.argmax(predictions, axis=1)
true_classes = np.argmax(y_test, axis=1)

#importo i moduli per la confusion matrix
from sklearn.metrics import confusion_matrix
import seaborn as sns

#plotto la matrice di confusione
conf_matrix = confusion_matrix(true_classes, predicted_classes)
plt.figure(figsize=(10,8))
sns.heatmap(conf_matrix, annot=True, fmt='d'
            , cmap='Blues')
plt.title('Matrice di Confusione')
plt.xlabel('Classe Predetta')
plt.ylabel('Classe Vera')
plt.show()

# 6 FACCIO UNA PREDIZIONE SU ALCUNE IMMAGINI DEL DATASET
# Seleziona un certo numero di immagini casuali dal test set
num_images = 3
random_indices = np.random.choice(len(X_test), num_images)

# Crea una figura per visualizzare le immagini e le predizioni
plt.figure(figsize=(15, 3))

# Loop sulle immagini selezionate casualmente
for i, idx in enumerate(random_indices):
    # Estrai l'immagine e la vera etichetta
    image = X_test[idx].reshape(28, 28)  # Rimodella l'immagine per visualizzarla (28x28)
    true_label = np.argmax(y_test[idx])  # Etichetta reale (non in one-hot encoding)
    
    # Fai la predizione sull'immagine
    prediction = model.predict(X_test[idx].reshape(1, 784))  # Risposta del modello
    predicted_label = np.argmax(prediction)  # Etichetta predetta
    
    # Mostra l'immagine
    plt.subplot(1, num_images, i+1)
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.title(f'T:{true_label}, P:{predicted_label}')  # T: etichetta vera, P: etichetta predetta

# Mostra tutte le immagini in una singola riga
plt.show()

