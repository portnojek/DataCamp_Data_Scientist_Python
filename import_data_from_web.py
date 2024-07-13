
# Wylaczenie certyfikacji SSL - tylko w celach diagnostycznych
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

# Import package
from urllib.request import urlretrieve

# Import pandas
import pandas as pd

# Assign url of file: url

url = 'https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Save file locally

urlretrieve(url, 'winequality-red.csv')

# Read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())