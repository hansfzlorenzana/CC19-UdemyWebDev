import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')
%matplotlib inline

dataset = 'UdemyWebDev_cleaned.csv'
data = pd.read_csv(dataset)

filter1 = 'Number of Ratings'
filter2 = 'Number of Students'
filter3 = 'Course Rating'

# Top 10 courses base on filters, either paid or free
data.sort_values([filter1,filter2,filter3],ascending=[False,False,False],inplace=True)

data[['Course Title','URL','Course Rating','Number of Ratings','Number of Students','Subscription Type']].head(10)

plt.figure(figsize=(8,6))
plt.rcParams['patch.force_edgecolor'] = True
data['Number of Ratings'].hist(bins=50)

plt.figure(figsize=(8,6))
plt.rcParams['patch.force_edgecolor'] = True
data['Course Rating'].hist(bins=50)

plt.figure(figsize=(8,6))
plt.rcParams['patch.force_edgecolor'] = True
sns.jointplot(x='Course Rating', y='Number of Ratings', data=data, alpha=0.4)