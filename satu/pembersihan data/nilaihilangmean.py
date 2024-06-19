import pandas as pd
import seaborn as sns

data = sns.load_dataset('tips')

# menangani data yang hilang dengan menggunakan nilai mean
data.fillna(data.mean(), inplace=True)

