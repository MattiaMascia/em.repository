from sklearn.datasets import load_iris
import pandas as pd
data = load_iris()
X = data.data # caratteristiche
y = data.target # target

print(X)
print(y)
df = pd.DataFrame(data)