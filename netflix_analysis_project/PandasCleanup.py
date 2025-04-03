import pandas as pd
import numpy as np

# Load the dataset into a Pandas DataFrame.
df = pd.read_csv('netflix_titles.csv')

# Check for and add up missing values in each column.
missing_values = df.isnull().sum()
print("\nMissing Data")
print(missing_values)

# Fill missing values in categorial columns.
df['director'] = df['director'].fillna('Empty')
df['cast'] = df['cast'].fillna('Empty')
df['country'] = df['country'].fillna('Empty')

# Drop rows with missing date_added.
df.dropna(subset=['date_added'], inplace=True)

# Count the number of unique values in each column.
unique_values = df.nunique()
print("\nUnique values in each column:")
print(unique_values)

# Find the most frequent movie type.
most_frequent_type = df['type'].mode()[0]
print(f"\nThe most frequent movie type is: {most_frequent_type}")

# Find the oldest and newest movies.
oldest_movie = df[df['release_year'] == df['release_year'].min()]
newest_movie = df[df['release_year'] == df['release_year'].max()]

print(f"\nThe oldest movie is: {oldest_movie['title'].values[0]} ({oldest_movie['release_year'].values[0]})")
print(f"The newest movie is: {newest_movie['title'].values[0]} ({newest_movie['release_year'].values[0]})")

# Calculate the year with the most titles released using NumPy.
unique_years, counts = np.unique(df['release_year'].values, return_counts=True)
year_with_most_titles = unique_years[np.argmax(counts)]
most_titles_count = np.max(counts)

print(f"\nThe year with the most titles released is: {year_with_most_titles} with {most_titles_count} titles.")

print("\n Cleaned data:")
filled_missing_values = df.isnull().sum()
print(filled_missing_values)
