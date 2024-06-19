import pandas as pd
import seaborn as sns

data=sns.load_dataset('tips')

df = data[data['total_bill']>10.00]
df['total_bill'].min()
df.head()