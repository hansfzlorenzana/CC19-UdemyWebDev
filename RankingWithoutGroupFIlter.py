import pandas as pd

dataset = 'UdemyWebDev_cleaned.csv'
data = pd.read_csv(dataset)

filter1 = 'Number of Ratings'
filter2 = 'Number of Students'
filter3 = 'Course Rating'

# Top 10 courses base on filters, either paid or free
data.sort_values([filter1,filter2,filter3],ascending=[False,False,False],inplace=True)

data[['Course Title','URL','Course Rating','Number of Ratings','Number of Students','Subscription Type']].head(10)

