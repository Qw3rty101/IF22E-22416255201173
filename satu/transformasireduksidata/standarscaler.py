import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler

data = sns.load_dataset('iris')

features = ['sepal_length', 'sepal_width']

scaler = StandardScaler()
data['features'] = scaler.fit_transform(data[features])
data.head()

