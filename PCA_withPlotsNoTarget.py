from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

# load dataset as pandas dataframe
dataset = "UdemyWebDev_cleaned.csv"
df = pd.read_csv(dataset)

features = ['Course Rating', 'Number of Ratings', 'Course Length', 'Number of Lectures','Number of Students','Price']

x = df.loc[:, features].values
x = StandardScaler().fit_transform(x)

np.mean(x),np.std(x)

pd.DataFrame(data = x, columns = features).head(2)

pca = PCA()

pca_out = pca.fit(x)

pca_out.explained_variance_ratio_

np.cumsum(pca_out.explained_variance_ratio_)

loadings = pca_out.components_
num_pc = pca_out.n_features_
pc_list = ["PC"+str(i) for i in list(range(1, num_pc+1))]
loadings_df = pd.DataFrame.from_dict(dict(zip(pc_list, loadings)))
loadings_df['variable'] = features
loadings_df = loadings_df.set_index('variable')
loadings_df

import seaborn as sns
import matplotlib.pyplot as plt
ax = sns.heatmap(loadings_df, annot=True, cmap='Spectral')
plt.show()

pca_out.explained_variance_ # get eigen_values

from bioinfokit.visuz import cluster
cluster.screeplot(obj=[pc_list, pca_out.explained_variance_ratio_])

# get PC scores
pca_scores = PCA().fit_transform(x)

# get 2D biplot
cluster.biplot(cscore=pca_scores, loadings=loadings, labels=features, var1=round(pca_out.explained_variance_ratio_[0]*100, 2),
    var2=round(pca_out.explained_variance_ratio_[1]*100, 2))