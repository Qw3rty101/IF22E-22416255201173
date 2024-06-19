import dask.dataframe as dd
import pandas as pd

df1 = dd.from_pandas(pd.DataFrame({
    'ID' : [1,2,3],
    'Name' : ['Alice', 'Bob', 'Charlie']
}),npartitions=2)

df2 = dd.from_pandas(pd.DataFrame({
    'ID' : [1,2,4],
    'Age' : [20,30,22]
}), npartitions=2)

merge_df = dd.merge(df1, df2, on='ID', how='inner')

print(merge_df)

