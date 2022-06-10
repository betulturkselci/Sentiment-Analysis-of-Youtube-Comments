import pandas as pd

# read_file = pd.read_csv (r'yorumlar.txt')
# read_file.to_csv (r'yorumlar.csv', index=None)

df = pd.read_json (r'reviews.json', lines=True) 
df.to_csv (r'reviews-dataset.csv', index = None)

