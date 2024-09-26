import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


data = load_diabetes()


#ASSEGNO LE VAR DIPENDENTI E LE VAR INDIPENDENTI
X = data.data  # VAR DIP
y = data.target  # VAR INDIP
df = pd.DataFrame(data=data.data, columns =data.feature_names)
print(df.head())

#STANDARDIZZO
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#SPLIT TRAIN/TEST
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

#SCELGO IL MODELLO
model = LinearRegression()

#UTILIZZO IL FIT PER ADDESTRARE IL MODELLO
model.fit(X_train, y_train)

#ESTRAGGO LE PREDIZIONI
y_pred = model.predict(X_test)

#MSE
mse = mean_squared_error(y_test, y_pred)

#R2
r2 = r2_score(y_test, y_pred)

#STAMPO I RISULTATI
print(f"MSE: {mse:.2f}")
print(f"R2: {r2:.2f}")

#STAMPO I COEFFICIENTI PER VEDERE QUALI SONO LE VARIABILI PIU CORRELATE
coefficients = model.coef_
print("Coefficienti:", coefficients)

#PLOTTO LE Y REALI VS LE Y PREDICT
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, edgecolor='k', color='blue', alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)  
plt.xlabel("Y Reali")
plt.ylabel("Y Predette")
plt.title("Regressione Lineare: Y vs Y-PRED")
plt.show()