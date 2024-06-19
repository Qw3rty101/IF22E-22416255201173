import pandas as pd
import re

df = pd.read_excel("data text (2).xlsx")
df.tail()

df.isnull().sum()

df.dropna(how='any', inplace=True)
df.isnull().sum

df['Text'] = df['Text'].apply(lambda x: re.sub('[^a-zA-z0-9\s]', '', x))
df.tail()

