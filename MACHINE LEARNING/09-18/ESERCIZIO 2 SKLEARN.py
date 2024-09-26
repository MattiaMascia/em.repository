from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.metrics import classification_report, confusion_matrix

#1 Carica il dataset Iris
data = load_iris()
X = data.data
y = data.target

#2 Standardizza le caratteristiche
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


#3 Suddividi i dati in training e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#4 Applico DecisionTreeClassifier
classifier = DecisionTreeClassifier(random_state=42)
classifier.fit(X_train, y_train)

#prevedo le etichette
y_pred = classifier.predict(X_test)
print(y_pred)

#5 Valuta la performance del modello utilizzando il classification_report(precisione, recall, F1-score)


report = classification_report(y_test, y_pred, target_names=data.target_names)
print("\nClassification Report:", report)

#6 Visualizza la matrice di confusione
conf_matrix = confusion_matrix(y_test, y_pred)
print(conf_matrix)

#plotto la matrice
plt.figure() 
plt.plot(y_test, y_pred) 
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues',xticklabels=data.target_names,yticklabels=data.target_names)
plt.title('Matrice di Confusione')
plt.ylabel('Etichette Reali')
plt.xlabel('Etichette Previste')
plt.show()




