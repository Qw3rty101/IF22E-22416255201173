import numpy as np
import seaborn as sns
import pandas as pd


data = sns.load_dataset('iris')

features = ['petal_length']

data[features] = np.log1p(data[features])
data.head

features = 'sepal_length'

data[features] = pd.cut(data[features], bins=3, labels=['Low', 'Medium', 'High'])
data.head()

