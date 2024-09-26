import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

# Carico il dataset
wine = load_wine()
X = wine.data
y = wine.target
print(X.shape,y.shape)

print(wine.DESCR)

df = pd.DataFrame(X, columns=wine.feature_names)
df['target'] = y
print("\n",df.head())
df.describe()

#Suddivido il dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

#creo un randomforest classifier
rf = RandomForestClassifier(random_state=42)

#definisco la griglia di iperparametri
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'criterion': ['gini' or 'entropy']
}

# Uso GridSearchCV per la ricerca degli iperparametri ottimali
grid_search = GridSearchCV(rf, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)

# Stampo i migliori iperparametri trovati
print("\nMigliori iperparametri trovati:", grid_search.best_params_)

# Uso il miglior modello trovato da GridSearchCV
best_rf = grid_search.best_estimator_

# Addestro il modello sul set di training
best_rf.fit(X_train, y_train)

# Previsioni sul set di test
y_pred = best_rf.predict(X_test)

# Calcolo delle metriche
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

# Stampo i risultati
print(f"Accuratezza: {accuracy:.4f}")
print(f"Precisione: {precision:.4f}")
print(f"Richiamo: {recall:.4f}")
print(f"F1: {f1:.4f}")

# Creo la matrice di confusione
conf_matrix = confusion_matrix(y_test, y_pred)

# Visualizzo la matrice di confusione con una heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=wine.target_names, yticklabels=wine.target_names)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title("Matrice di Confusione")
plt.show()

# Report di classificazione
print("\nReport di classificazione:\n")
print(classification_report(y_test, y_pred, target_names=wine.target_names))

# Importanza delle caratteristiche
importances = best_rf.feature_importances_
indices = np.argsort(importances)[::-1]

# Stampa delle caratteristiche ordinate per importanza
print("\nLe caratteristiche più importanti in ordine decrescente sono:")
#misura quanto ogni caratteristica è stata utile nel predire correttamente l'output
#quanto ciascuna caratteristica è influente nel determinare la classe
for i in indices:
    print(f"{wine.feature_names[i]}: {importances[i]:.4f}")

# Visualizzo l'importanza delle caratteristiche
plt.figure(figsize=(10, 6))
plt.title("Importanza delle caratteristiche")
plt.bar(range(X.shape[1]), importances[indices], align="center")
plt.xticks(range(X.shape[1]), [wine.feature_names[i] for i in indices], rotation=90)
plt.tight_layout()
plt.show()

from sklearn.decomposition import PCA

# Applica la PCA per ridurre le dimensioni a tutte le componenti (manteniamo tutte per spiegare la varianza)
pca = PCA()
X_pca = pca.fit_transform(X)

# Calcola la varianza spiegata cumulativa
explained_variance = pca.explained_variance_ratio_
cumulative_variance = np.cumsum(explained_variance)

# Trova il numero minimo di componenti per spiegare almeno il 70% della varianza
n_components_70 = np.argmax(cumulative_variance >= 0.70) + 1  # +1 perché np.argmax restituisce l'indice
print(f"\nNumero di componenti per spiegare almeno il 70% della varianza: {n_components_70}")

# Stampa la varianza spiegata da ciascuna componente
print("\nVarianza spiegata da ciascuna componente principale:")
for i in range(len(explained_variance)):
    print(f"Componente {i+1}: {explained_variance[i]:.4f} (Cumulativo: {cumulative_variance[i]:.4f})")

# Mostra quali caratteristiche contribuiscono maggiormente a ciascuna componente
print("\nContributi delle caratteristiche originali per le prime componenti principali:")
for i in range(n_components_70):
    print(f"\nComponente {i+1}:")
    for j in np.argsort(np.abs(pca.components_[i]))[::-1]:  # Ordina in base al contributo assoluto
        print(f"{wine.feature_names[j]}: {pca.components_[i, j]:.4f}")
