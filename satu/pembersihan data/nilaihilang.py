import pandas as pd
import seaborn as sns

data = sns.load_dataset('tips')

# mengidentifikasi nilai hilang
missing_values = data.isnull().sum()
print("Jumlah data hilang: ")
print(missing_values)