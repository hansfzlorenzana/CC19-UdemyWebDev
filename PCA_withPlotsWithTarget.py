from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
from bioinfokit.visuz import cluster

# load dataset as pandas dataframe
dataset = "UdemyWebDev_cleaned.csv"
df = pd.read_csv(dataset)

groupBy = 'Difficulty' # the target attribute/group
target = df[groupBy].to_numpy()

features = ['Course Rating', 'Number of Ratings', 'Course Length', 'Number of Lectures','Number of Students','Price']

X = df.loc[:, features]
print(X.head(2))
x = StandardScaler().fit_transform(X)

pca = PCA()
pca_out = pca.fit(x)

loadings = pca_out.components_

pca_out.explained_variance_ # get eigen_values

# get PC scores
pca_scores = PCA().fit_transform(x)

# get 2D biplot
cluster.biplot(cscore=pca_scores, loadings=loadings, labels=X.columns.values, var1=round(pca_out.explained_variance_ratio_[0]*100, 2),
    var2=round(pca_out.explained_variance_ratio_[1]*100, 2), colorlist=target)