from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
import pandas as pd
import seaborn as sns

data = sns.load_dataset('iris')

features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
x = data[features]
x_standardized = StandardScaler().fit_transform(x)

tsne = TSNE(n_components=2, perplexity=30)
tsne_result = tsne.fit_transform(x_standardized)
tsne_df = pd.DataFrame(tsne_result, columns=['t-SNE1', 't-SNE2'])

tsne_df.head()


