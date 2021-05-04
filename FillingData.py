
import pandas as pd

pd.set_option('display.max_columns', None)

df = pd.read_csv('Crime_Data_from_2010_to_Present_Original.csv', parse_dates=['Date Occurred'])

new_df = df.fillna({
'Crime Code Description' : 'no description',
'MO Codes' : "0",
'Victim Sex' : "U",
'Victim Descent' : "X",
'Premise Code' : 0,
'Premise Description' : "no data",
'Weapon Used Code' : 0,
'Weapon Description' : "no data",
'Status Code' : "0",
'Status Description' : "no data",
'Crime Code 1' : 0,
'Crime Code 2' : 0,
'Crime Code 3' : 0,
'Crime Code 4' : 0,
'Address': "no data",
'Cross Street': "no data"
})


# Create a groupby object: by_sex_descent
by_sex_descent = new_df.groupby(['Victim Sex', 'Victim Descent'])

# Write a function that imputes median
def impute_median(series):
    return series.fillna(series.median())

# Impute age
new_df['Victim Age'] = by_sex_descent['Victim Age'].transform(impute_median)



new_df['Longitude'], new_df['Latitude'] = new_df['Location '].str.split(',', 1).str


new_df['Longitude'] = new_df['Longitude'].str.strip()
new_df['Longitude'] = new_df['Longitude'].str.replace(r"^\D", '', case=False)

new_df['Latitude'] = new_df['Latitude'].str.strip()
new_df['Latitude'] = new_df['Latitude'].str.replace(r"\D$", '', case=False)


#interpolate lon and lat

new_df['Longitude'] = new_df['Longitude'].interpolate()
new_df['Latitude'] = new_df['Latitude'].interpolate()



new_df.to_csv('Clean_CrimeDataset.csv', sep='\t', encoding='utf-8')