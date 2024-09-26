from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
#  Importa la funzione train_test_split dal modulo
# sklearn.model_selection. Questa funzione viene utilizzata per suddividere il
# dataset in due insiemi: uno per l'addestramento (training set) e uno per il test
# (test set).


# 1. Carica il dataset Iris
data = load_iris()
X = data.data
y = data.target

# 2. Suddividi i dati in training e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Applica l'algoritmo K-Nearest Neighbors con n_neighbors=5
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# 4. Valuta la performance del modello usando l'accuratezza
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuratezza del modello: {accuracy:.2f}")