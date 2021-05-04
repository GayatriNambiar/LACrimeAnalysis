import pandas as pd
import re

df = \
    pd.read_csv('IBM-HR-Employee-Attrition.csv')


line = re.sub('[!@#$]', '', df['Location'])