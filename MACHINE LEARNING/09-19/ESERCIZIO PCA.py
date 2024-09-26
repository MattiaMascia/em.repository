#ESERCIZIO A PAGINA 366
import numpy as np
import pandas as pd

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, RandomizedSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from scipy.stats import randint as sp_randint
from scipy.stats import uniform

#carico il dataset
data = load_wine()
X = data.data
y = data.target

#Standardizzo
scaler = StandardScaler()
scaled_features = scaler.fit_transform(data.data)
df_scaled = pd.DataFrame(data=scaled_features, columns=data.feature_names)
df_scaled['target'] = data.target
print(f"\nI tuoi dati standardizzati sono:\n {df_scaled.head()}")

#Suddivido in training e test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)


#Riduco la dimensionalità mantenendo il 95% della varianza
pca = PCA(n_components=0.95)

#Gradient Boosting Classifier 
gbc = GradientBoostingClassifier()

#definisco la pipeline
pipeline = Pipeline([
    ('scaler', scaler),
    ('pca', pca),
    ('gbc', gbc)#mi serve a migliorare la pca e si basa su diverse di tecniche alberi di classificazione concatenati
])

#Definisco la griglia di distanza
param_dist = {
    'pca__n_components': sp_randint(5, 13),#numero delle componenti principali
    'gbc__n_estimators': sp_randint(50, 200),#numero di alberi nel gradient boosting
    'gbc__learning_rate': uniform(0.01, 0.2),#definisco il tasso di apprendimento
    'gbc__max_depth': sp_randint(1, 5),#profondità massima degli alberi
    'gbc__subsample': uniform(0.6, 0.4), #ridurre può aiutare a migliorare over-underfitting
    'gbc__min_samples_split': sp_randint(2, 10),#numero minimo di campioni per suddividere un nodo
    'gbc__min_samples_leaf': sp_randint(1, 10),#valori più grandi creano alberi più semplici, utile a gestire over e underfiiting
    'gbc__max_features': ['auto', 'sqrt', 'log2', None]#numero massimo di iterazione (per evitare overfitting)
}


#utilizzo RandomizedSearchCV per migliorare gli iperparametri
rdm = RandomizedSearchCV(pipeline, param_distributions=param_dist, random_state=42)#migliori iperparametri in modo efficiente


#StratifiedKFold
skf = StratifiedKFold(n_splits=5)

# Suddividi i dati in training e test set (70% training, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)

# Addestra il modello utilizzando RandomizedSearchCV
rdm.fit(X_train, y_train)

# Fai previsioni sul test set
y_pred = rdm.predict(X_test)

#valuto le prestazioni del modello
print("Classification Report:\n", classification_report(y_test, y_pred, target_names=data.target_names))

#Migliori iperparametri trovati da RandomizedSearchCV
print("Migliori parametri trovati:\n", rdm.best_params_)

