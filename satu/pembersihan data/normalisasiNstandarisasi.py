import pandas as pd
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

data = sns.load_dataset('tips')

scaler = MinMaxScaler()

data_sc = scaler.fit_transform(data)
data = pd.DataFrame(data_sc, columns = data.columns)

data.head()

