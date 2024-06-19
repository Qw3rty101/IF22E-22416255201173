from sklearn.discriminant_analysis import LinearDisccriminantAnalysis
from sklearn.preprocessing import StandardScaler
import pandas as pd
import seaborn as sns

data = sns.load_dataset('iris')

features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
x = data[features]
x_standardized = StandardScaler().fit_transform(x)

lda = LDA(n_components=2, perplexity=30)
lda_result = lda.fit_transform(x_standardized)
lda_df = pd.DataFrame(lda_result, columns=['t-SNE1', 't-SNE2'])

lda_df




