import pandas as pd

df = \
    pd.read_csv('IBM-HR-Employee-Attrition.csv')

# print("1. Find the number of entries/rows and columns in the data.")
# print("Number of rows: " + str(len(df)))
# print("Number of columns: " + str(len(df.columns)))
#
# print('\n')
#
# print("2. What is the average Monthly Income")
# print(df['MonthlyIncome'].mean())
#
# print('\n')
#
# print("3. What is the highest amount of HourlyRate")
# print(df['HourlyRate'].max())
#
# print('\n')
#
# print("4. What is the Department, JobRole, MaritalStatus and OverTime of EmployeeNumber 10.")
# df.set_index('EmployeeNumber', inplace=True)
# print(df.loc[10, ['Department', 'JobRole', 'MaritalStatus', 'OverTime']])
#
# print('\n')
#
# print("5. What is the Employee ID of highest MonthlyIncome paid employee?")
# print(df.loc[df['MonthlyIncome'] == df['MonthlyIncome'].max(), ['MonthlyIncome']])
#
#
# print('\n')
#
# print("6. What is the Average (mean) DailyRate for all Employees Group By Age whose age is greater than 58. (hint: use groupby function)")
# print(df._where(df['Age'] > 58).groupby('Age')['DailyRate'].mean())
#
# print('\n')
#
# print("7. How many unique EducationField are there?")
# print(df['EducationField'].nunique())
#
# print('\n')
#
# print("8. What are the top 5 most common JobRole?")
# print(df.groupby('JobRole').size().nlargest(5))
#
# print('\n')
#
# print("9. How many JobRoles represented by less than 100 employees?")
# count = df.groupby('JobRole').size()
# print(len(count[count < 100]))
#
# print('\n')
#
# print("10. What is the correlation between Education and JobSatisfaction?")
# print(df['Education'].corr(df['JobSatisfaction']))

# print(df.head())

# df['A'], df['B'] = df['EducationField'].str.split(' ', 1).str

df['Department'] = df['Department'].str.replace('&', ' ', case=False)

print(df.head())