import pandas as pd
import os
import datetime

df = pd.read_csv('Project12BSSWelcomeCallWithoutRD140225.csv', header=None)


date_column_name = 2
df [date_column_name] = pd.to_datetime(df[date_column_name], errors='coerce').dt.strftime('%d/%m')
column_name = 3
unique_values = df[column_name].unique
outputdirectory = 'test'
os.makedirs(outputdirectory, exist_ok=True)