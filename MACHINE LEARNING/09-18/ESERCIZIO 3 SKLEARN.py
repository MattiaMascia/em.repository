import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

#1 Carico il dataset
wine = load_wine()
df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
df['target'] = wine.target
print(f"\nI tuoi dati sono:\n {df.head()}")

import matplotlib.pyplot as plt


plt.figure(figsize=(14, 10))
#istogramma per ciascuna caratteristica
for i, feature in enumerate(wine.feature_names):
    plt.subplot(4, 4, i + 1)  # sceglie la posizione del subplot
    plt.hist(df[feature], bins=30, alpha=0.7, label='Originale')#feature è il nome della caratteristica
    plt.title(feature)
    plt.xlabel('Valore')
    plt.ylabel('Frequenza')
    plt.grid(True)

plt.tight_layout()
plt.suptitle('Distribuzione delle Caratteristiche Originali', y=1.02)
plt.show()


#2 Standardizzo le caratteristiche
scaler = StandardScaler()
scaled_features = scaler.fit_transform(wine.data)
df_scaled = pd.DataFrame(data=scaled_features, columns=wine.feature_names)
df_scaled['target'] = wine.target
print(f"\nI tuoi dati standardizzati sono:\n {df_scaled.head()}")


# Imposta la dimensione dei grafici
plt.figure(figsize=(14, 10))

# Crea un istogramma per ciascuna caratteristica standardizzata
for i, feature in enumerate(wine.feature_names):
    plt.subplot(4, 4, i + 1)  # sceglie la posizione del subplot
    plt.hist(df_scaled[feature], bins=30, alpha=0.7, label='Standardizzato')#feature è il nome della caratteristica
    plt.title(feature)
    plt.xlabel('Valore')
    plt.ylabel('Frequenza')
    plt.grid(True)

plt.tight_layout()
plt.suptitle('Distribuzione delle Caratteristiche Standardizzate', y=1.02)
plt.show()


#3 Suddivido i dati in training set e test set
X_train, X_test, y_train, y_test = train_test_split(scaled_features, wine.target, test_size=0.3, random_state=42)

# 4 Applico un algortimo di classificazione
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)
#faccio previsione
y_pred = clf.predict(X_test)
y_pred_labels = [wine.target_names[pred] for pred in y_pred]
y_test_labels = [wine.target_names[true] for true in y_test]

print(f"\nQueste sono le previsioni sulle y: {y_pred_labels}")
print(f"\nQueste sono le etichette reali: {y_test_labels}")

# 5 Valuta il classificatore
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuratezza: {accuracy:.2f}")
print("\nReport di classificazione:")
print(report)

import seaborn as sns
from sklearn.metrics import confusion_matrix

#6 calcolo la matrice di confusione
conf_matrix = confusion_matrix(y_test, y_pred)

#plotto la matrice
plt.figure() 
plt.plot(y_test, y_pred) 
sns.heatmap(conf_matrix, annot=True, cmap='Blues',xticklabels=wine.target_names,yticklabels=wine.target_names)
plt.title('Matrice di Confusione')
plt.ylabel('Etichette Reali')
plt.xlabel('Etichette Previste')
plt.show()



