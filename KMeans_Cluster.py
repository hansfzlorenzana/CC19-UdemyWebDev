import pandas as pd
from yellowbrick.cluster import KElbowVisualizer
from sklearn.cluster import KMeans
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt

# load dataset as pandas dataframe
dataset = "UdemyWebDev_cleaned.csv"
df = pd.read_csv(dataset)

features = ['Course Rating', 'Number of Ratings', 'Course Length', 'Number of Lectures','Number of Students','Price']

X = df.loc[:, features]

# change values according to attributes to visualize
var1 = 'Number of Lectures'
var2 = 'Number of Students'

model = KMeans()
visualizer = KElbowVisualizer(model, k=(1,12)).fit(X)
visualizer.show()

# change n_clusters according to elbow method optimal cluster count
kmeans = KMeans(n_clusters=3, init='k-means++', random_state=0).fit(X)

kmeans.labels_
kmeans.inertia_
kmeans.n_iter_
kmeans.cluster_centers_
print(Counter(kmeans.labels_))

sns.scatterplot(data=X, x=var1, y=var2, hue=kmeans.labels_)
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], 
            marker="X", c="r", s=80, label="centroids")
plt.legend()
plt.show()
