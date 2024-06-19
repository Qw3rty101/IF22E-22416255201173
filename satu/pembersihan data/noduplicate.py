import pandas as pd
import seaborn as sns

data = sns.load_dataset('tips')

# penanganan duplikai data
data.drop_duplicates(inplace=True)