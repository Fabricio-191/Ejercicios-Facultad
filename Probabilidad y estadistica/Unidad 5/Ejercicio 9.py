import pandas as pd 
import seaborn as sns
import numpy as np

sns.get_dataset_names()
df1=sns.load_dataset("iris")

print(df1.describe())

# Determinar el estimador puntual para la media de sepal_length.
print("Media de sepal_length")
print(df1.sepal_length.mean())

# Determinar el estimador puntual para la varianza de petal_width.
print("Varianza de petal_width")
print(df1.petal_width.var())
