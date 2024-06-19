import pandas as pd
import seaborn as sns

data = sns.load_dataset('tips')

data.head()

# menangani outliners, mengidentifikasi dan menangani nilai-nilai yang extreme yang mungkin mempengaruhi analisis. Mengidentifikasi dengan boxplot
# sns.boxenplot(data, y='total_bill')


# Menghapus outliner dengan zscore
data['total_bill_Z'] = (data['total_bill']-data['total_bill'].mean()/data['total_bill'].std())
data.head()

# data_no = data[(data['total_bill_Z']<2)]
# data_no.head()

# lanjut halaman 34
