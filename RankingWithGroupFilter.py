import pandas as pd

dataset = 'UdemyWebDev_cleaned.csv'
data = pd.read_csv(dataset)

filter1 = 'Number of Ratings'
filter2 = 'Number of Students'
filter3 = 'Course Rating'
group_value = 'Free' # can be turned into user input

# Top 10 FREE courses base on highest number of ratings and highest rating
freeCourses = data.loc[data['Subscription Type']== group_value]
freeCourses.sort_values([filter1,filter2,filter3],ascending=[False,False,False],inplace=True)

freeCourses[['Course Title','URL','Course Rating','Number of Ratings','Number of Students','Subscription Type','Price']].head(10)



