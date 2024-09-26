import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

temperature = np.random.uniform(low=0, high=35, size=30)

df = pd.DataFrame({'temperature': temperature})

print(df.head())
temp_max = df['temperature'].max()       
temp_min = df['temperature'].min()        
temp_mean = df['temperature'].mean()      
temp_median = df['temperature'].median()  

# Stampa delle statistiche
print(f"Temperatura massima: {temp_max:.2f}")
print(f"Temperatura minima: {temp_min:.2f}")
print(f"Temperatura media: {temp_mean:.2f}")
print(f"Mediana delle temperature: {temp_median:.2f}")


x = df.index + 1  
y = df['temperature']  

# GRAFICO A LINEE
plt.figure()  
plt.plot(x, y)  
plt.title('Temperatura Giornaliera per un Mese')
plt.xlabel('Giorno del Mese')
plt.ylabel('Temperatura')
plt.grid(True) #se voglio aggiungere una graglia
plt.show()

# SCATTER PLOT
plt.figure()
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('Temperatura')
plt.ylabel('Giorno del mese')
plt.show()

#ISTOGRAMMA
plt.figure()
plt.hist(y, bins=35)
plt.title('Istogramma')
plt.xlabel('Temperatura')
plt.ylabel('Frequenza')
plt.show()

# GRAFICO A BARRE
plt.figure()
plt.bar(x, y)  
plt.title('Grafico a Barre')
plt.xlabel('Giorno del Mese')
plt.ylabel('Temperatura')
plt.grid(True)
plt.show()