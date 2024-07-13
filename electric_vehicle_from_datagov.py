import csv
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
df = pd.read_csv('Electric_Vehicle_Population_Data.csv', delimiter=';')

print(df.head())