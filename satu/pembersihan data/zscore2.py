import pandas as pd
import seaborn as sns

data = sns.load_dataset('tips')

# Menghapus outliner dengan zscore
data['total_bill_Z'] = (data['total_bill']-data['total_bill'].mean()/data['total_bill'].std())
data.head()

# data_no = data[(data['total_bill_Z']<2)]
# data_no.head()

sns.boxplot(data, y='total_bill')
