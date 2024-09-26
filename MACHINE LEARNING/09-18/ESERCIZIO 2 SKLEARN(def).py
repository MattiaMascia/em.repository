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
def load_dataset():
    data = load_iris()
    x = data.data
    y = data.target
    return x,y,data

#2 Standardizza le caratteristiche
def standard(x):
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)
    return x_scaled

#3 Suddividi i dati in training e test
def split(x,y, test_size=0.3, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size, random_state)
    return X_train,X_test,y_train,y_test

#4 Applico DecisionTreeClassifier
def decision_tree(X_train, y_train, random_state=42):
    classifier = DecisionTreeClassifier(random_state)
    classifier.fit(X_train, y_train)
    return classifier

def prediction(X_test, classifier ):
    y_pred = classifier.predict(X_test)
    print(f"Le tue etichette previste sono{y_pred}")
    return y_pred

#5 Valuta la performance del modello utilizzando il classification_report(precisione, recall, F1-score)
def reportage(y_test, y_pred, data):
    report = classification_report(y_test, y_pred, target_names=data.target_names)
    print("\nClassification Report:", report)
    return report

