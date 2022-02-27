import matplotlib.pyplot as plt
import numpy as np
from sentence_transformers import SentenceTransformer
import pandas as pd
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA

plt.style.use('ggplot')
plt.rcParams['font.family'] = 'sans-serif' 
plt.rcParams['font.serif'] = 'Ubuntu' 
plt.rcParams['font.monospace'] = 'Ubuntu Mono' 
plt.rcParams['font.size'] = 14 
plt.rcParams['axes.labelsize'] = 12 
plt.rcParams['axes.labelweight'] = 'bold' 
plt.rcParams['axes.titlesize'] = 12 
plt.rcParams['xtick.labelsize'] = 12 
plt.rcParams['ytick.labelsize'] = 12 
plt.rcParams['legend.fontsize'] = 12 
plt.rcParams['figure.titlesize'] = 12 
plt.rcParams['image.cmap'] = 'jet' 
plt.rcParams['image.interpolation'] = 'none' 
plt.rcParams['figure.figsize'] = (12, 10) 
plt.rcParams['axes.grid']=True
plt.rcParams['lines.linewidth'] = 2 
plt.rcParams['lines.markersize'] = 8
colors = ['xkcd:pale orange', 'xkcd:sea blue', 'xkcd:pale red', 'xkcd:sage green', 'xkcd:terra cotta', 'xkcd:dull purple', 'xkcd:teal', 'xkcd: goldenrod', 'xkcd:cadet blue',
'xkcd:scarlet']

dataset = 'UdemyWebDev_cleaned.csv'

data = pd.read_csv(dataset)

X = np.array(data['Course Description'])

data = data[['Instructor','Course Description','Course Title']]

data.head()

text_data = X
model = SentenceTransformer('distilbert-base-nli-mean-tokens')
embeddings = model.encode(text_data, show_progress_bar=True)

X = np.array(embeddings)
n_comp = 5
pca = PCA(n_components=n_comp)
pca.fit(X)
pca_data = pd.DataFrame(pca.transform(X))
pca_data.head()

cos_sim_data = pd.DataFrame(cosine_similarity(X))

def give_recommendations(index,print_recommendation = False,print_recommendation_plots= False,print_genres =False):
  index_recomm =cos_sim_data.loc[index].sort_values(ascending=False).index.tolist()[1:6]
  movies_recomm =  data['Course Title'].loc[index_recomm].values
  result = {'Courses':movies_recomm,'Index':index_recomm}
  if print_recommendation==True:
    print('The subscribed course is this one: %s \n'%(data['Course Title'].loc[index]))
    k=1
    for movie in movies_recomm:
      print('The number %i recommended course is this one: %s \n'%(k,movie))
  if print_recommendation_plots==True:
    print('The description of the subscribed course is this one:\n %s \n'%(data['Course Description'].loc[index]))
    k=1
    for q in range(len(movies_recomm)):
      plot_q = data['Course Description'].loc[index_recomm[q]]
      print('The description of the number %i recommended course is this one:\n %s \n'%(k,plot_q))
      k=k+1
  if print_genres==True:
    print('The instructor/s of the subscriber course is this one:\n %s \n'%(data['Instructor'].loc[index]))
    k=1
    for q in range(len(movies_recomm)):
      plot_q = data['Instructor'].loc[index_recomm[q]]
      print('The description of the number %i recommended course is this one:\n %s \n'%(k,plot_q))
      k=k+1
  return result

plt.figure(figsize=(20,20))
for q in range(1,5):
  plt.subplot(2,2,q)
  index = np.random.choice(np.arange(0,len(X)))
  to_plot_data = cos_sim_data.drop(index,axis=1)
  plt.plot(to_plot_data.loc[index],'.',color='firebrick')
  recomm_index = give_recommendations(index)
  x = recomm_index['Index']
  y = cos_sim_data.loc[index][x].tolist()
  m = recomm_index['Courses']
  plt.plot(x,y,'.',color='navy',label='Recommended Courses')
  plt.title('Courses Subscribed: '+data['Course Title'].loc[index])
  plt.xlabel('Course Index')
  k=0
  for x_i in x:
    plt.annotate('%s'%(m[k]),(x_i,y[k]),fontsize=10)
    k=k+1

  plt.ylabel('Cosine Similarity')
  plt.ylim(0,1)

give_recommendations(2,True)

recomm_list = []
for i in range(len(X)):
  recomm_i = give_recommendations(i)
  recomm_list.append(recomm_i['Courses'])
recomm_data = pd.DataFrame(recomm_list,columns=['First Recommendation','Second Recommendation','Third Recommendation','Fourth Recommendation','Fifth Recommendation'])
recomm_data['Course Subscribed'] = data['Course Title']
recomm_data = recomm_data[['Course Subscribed','First Recommendation','Second Recommendation','Third Recommendation','Fourth Recommendation','Fifth Recommendation']]

recomm_data
