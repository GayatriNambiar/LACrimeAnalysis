import pandas as pd

df = pd.read_csv('Crime_Data_from_2010_to_Present_Original.csv', parse_dates=['Date Occurred'])
pd.set_option('display.max_columns', None)                             #displays all columns

print("==================Head========================")
print(df.head())
#
print("==================Tail========================")
print(df.tail())

print("==================Columns========================")
print(df.columns)

print("==================Shape========================")
print(df.shape)

print("==================Info========================")
print(df.info())