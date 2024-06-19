import pandas as pd
import seaborn as sns

data=sns.load_dataset('tips')

data['sex']=pd.to_numeric(data['sex'], errors='coerce')

data.dtypes