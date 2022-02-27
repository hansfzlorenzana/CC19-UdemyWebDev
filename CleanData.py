import pandas as pd

df = pd.read_csv("UdemyWebDev.csv")

# Drop ID column
data = df.drop('Course ID', axis=1) # Delete 'ID' column

# Drop all duplicate rows, considering ID column is now deleted
data.loc[data.duplicated(keep=False), :]
data.drop_duplicates(inplace=True)
data.drop_duplicates(subset='URL',keep='first',inplace=True)

# Removing substrings of 'Number of Ratings' then convert to numeric dtype
data['Number of Ratings']=data['Number of Ratings'].dropna().str.replace(',','').astype(int)

# Removing substrings of 'Number of Lectures' then convert to numeric dtype
data['Number of Lectures']=data['Number of Lectures'].dropna().str.replace('lectures','').str.replace(',','').astype(int)

# Removing substrings of 'Number of Students' then convert to numeric dtype
data['Number of Students']=data['Number of Students'].dropna().str.replace('students','').str.replace('student','').str.replace(',','').astype(int)

# Removing substrings of 'Price' then convert to numeric dtype
data['Price']=data['Price'].dropna().str.replace(',','').str.replace('Free','0').str.replace('ree','0').astype(int)

# Removing substrings of 'Course Length', converting mins to hours and converting to numeric dtype
data['Course Length']=data['Course Length'].dropna().str.replace('total hours','').str.replace('total hour','')
convertMinsToHours = round(data.loc[data['Course Length'].str.contains('total min')]['Course Length'].str.replace('total mins','').astype(float)/60,1)
data['Course Length'].mask(data['Course Length'].str.contains('total min'), convertMinsToHours, inplace=True)
data['Course Length']=data['Course Length'].astype(float)

# Replace incorrect 'True' values on 'subscription type' column with 'False' if price is 0
data.loc[data['Price']==0,'Subscription Type'] = False

# Replacing missing values
medianA = data['Course Rating'].median()
medianB = data['Number of Ratings'].median()
medianC = data['Number of Students'].median()

data['Course Rating'].fillna(medianA, inplace=True)
data['Number of Ratings'].fillna(medianB, inplace=True)
data['Number of Students'].fillna(medianC, inplace=True)

# Transform values of 'Subscription Type'
data['Subscription Type']=data['Subscription Type'].astype(str)
data['Subscription Type']=data['Subscription Type'].str.replace('True','Paid')
data['Subscription Type']=data['Subscription Type'].str.replace('False','Free')

data.to_csv('UdemyWebDev_cleaned.csv', index=False) # Save to CSV