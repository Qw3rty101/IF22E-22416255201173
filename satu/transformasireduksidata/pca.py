from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
import seaborn as sns

data = sns.load_dataset('iris')

features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
x = data[features]
x_standardized = StandardScaler().fit_transform(x)

pca = PCA(n_components=2)
principal_components = pca.fit_transform(x_standardized)
principal_df = pd.DataFrame(principal_components, columns=['PC1', 'PC2'])
principal_df.head()


