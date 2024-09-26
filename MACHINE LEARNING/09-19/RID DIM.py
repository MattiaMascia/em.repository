import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#CARICO IL DATASET
digits = load_digits()
X = digits.data
y = digits.target
target_names = digits.target_names
df = pd.DataFrame(data=digits.data, columns=digits.feature_names)
print(df.head())

#CON INDEX DECIDO QUALE IMMAGINE VISUALIZZARE, IN QUESTO CASO LA PRIMA
index = 0
image = digits.images[index]
label = digits.target[index]

#PLOTTO L'IMMAGINE
plt.figure(figsize=(4, 4))
plt.imshow(image, cmap=plt.cm.green_r, interpolation='nearest')
plt.title(f'Label: {label}')
plt.axis('off')  # Nasconde gli assi
plt.show()

#APPLICO LA PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

#VISUALIZZO I DATI DELLA PCA
plt.figure(figsize=(10, 6))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='tab10', edgecolor='k', s=50)
plt.title("PCA dei dati")
plt.xlabel("Prima componente principale")
plt.ylabel("Seconda componente principale")
plt.show()

#TRAIN/TEST
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#FACCIO UNA REGRESSIONE LOGISTICA
clf_original = LogisticRegression(max_iter=1000, random_state=42)
clf_original.fit(X_train, y_train)
y_pred_original = clf_original.predict(X_test)

#CALCOLO L'ACCURATEZZA SUI DATI ORGINALI
accuracy_original = accuracy_score(y_test, y_pred_original)
print(f"Accuratezza sui dati originali: {accuracy_original:.4f}")


#SUDDIVIDO IL DATASET RIDOTTO
X_train_pca, X_test_pca, y_train_pca, y_test_pca = train_test_split(X_pca, y, test_size=0.3, random_state=42)

#FACCIO UNA REGRESSIONE LOGISTICA SUL MODELLO RIDOTTO
clf_pca = LogisticRegression(max_iter=10000, random_state=42)
clf_pca.fit(X_train_pca, y_train_pca)
y_pred_pca = clf_pca.predict(X_test_pca)

#CALCOLO L'ACCURATEZZA SUI DATI RIDOTTI CON PCA
accuracy_pca = accuracy_score(y_test_pca, y_pred_pca)
print(f"Accuratezza sui dati ridotti con PCA: {accuracy_pca:.4f}")