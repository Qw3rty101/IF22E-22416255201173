import pandas as pd
import seaborn as sns

data = sns.load_dataset('tips')

# menangani outliners, mengidentifikasi dan menangani nilai-nilai yang extreme yang mungkin mempengaruhi analisis. Mengidentifikasi dengan boxplot
sns.boxenplot(data, y='total_bill')
