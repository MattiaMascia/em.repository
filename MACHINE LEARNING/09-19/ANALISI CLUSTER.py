#ninit = 4
#max_iter = abbassa il default
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import adjusted_rand_score, homogeneity_score
from sklearn.metrics import confusion_matrix, accuracy_score
from scipy.stats import mode
from sklearn.preprocessing import StandardScaler

# CARICO IL DATASET
data = load_iris()
X = data.data
y = data.target
target_names = data.target_names
df = pd.DataFrame(data=data.data, columns=data.feature_names)
print("\n", df.head())
print("\n", target_names)

# STANDARDIZZAZIONE
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# KMEANS
kmeans = KMeans(n_clusters=3, init='k-means++', n_init=4, max_iter=220, random_state=42)
y_kmeans = kmeans.fit_predict(X_scaled)

# UTILIZZO LA PCA PER LE PRIME 2 COMPONENTI PRINCIPALI
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# PLOTTO LE PRIME DUE COMPONENTI PRINCIPALI
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=y_kmeans, palette='viridis', s=100)
plt.title("Cluster ottenuti con K-Means (PCA 2D)")
plt.xlabel('Prima componente principale')
plt.ylabel('Seconda componente principale')
plt.show()

# PLOTTO I CLUSTER CREATI
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=y, palette='bright', s=100)
plt.title("Specie originali (PCA 2D)")
plt.xlabel('Prima componente principale')
plt.ylabel('Seconda componente principale')
plt.show()

# VALUTO IL MODELLO
ari = adjusted_rand_score(y, y_kmeans)  # Valuta la somiglianza tra le etichette predette e quelle reali
homogeneity = homogeneity_score(y, y_kmeans)  # Misura quanto i cluster contengano solo punti di una singola classe

print(f"Adjusted Rand Index: {ari:.4f}")
print(f"Homogeneity Score: {homogeneity:.4f}")

# MATRICE DI CONFUSIONE
conf_matrix = confusion_matrix(y, y_kmeans)

# PLOTTO
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=['Cluster 1', 'Cluster 2', 'Cluster 3'], yticklabels=target_names)
plt.title("Matrice di Confusione tra Etichette Reali e Cluster K-Means")
plt.ylabel("Etichette Reali")
plt.xlabel("Cluster K-Means Assegnati")
plt.show()

# RIASSEGNO AD OGNI CLUSTER L'ETICHETTA
etichette = np.zeros_like(y_kmeans)
for i in range(3):
    mask = (y_kmeans == i)
    etichette[mask] = mode(y[mask])[0]

accuracy = accuracy_score(y, etichette)
print(f"Accuracy: {accuracy:.4f}")