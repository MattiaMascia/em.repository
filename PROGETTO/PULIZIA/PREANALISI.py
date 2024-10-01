import pandas as pd
import ast
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

df = pd.read_csv("PROGETTO/movies_metadata_CLEAN.csv")
print("\n",df.head())
print("\n",df.describe())
print("\n",df.shape)

# true_count = df['adult'].sum()#avevo provato così ma non so cosa legge
# print(true_count)

true_count = (df['adult'] == 'True').sum()
#sono 0 quindi elimino la colonna
df.drop(columns='adult', inplace=True)

#sposto id in prima colonna
cols = list(df.columns)
cols.insert(0, cols.pop(cols.index('id')))
df = df[cols]
print(df.head())


