import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset into a Pandas DataFrame.
df = pd.read_csv('netflix_titles.csv')

# Charts work better with original data set, otherwise the filled, unknown fields dominate the charts.

country_counts = df['country'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(country_counts.head(10).index, country_counts.head(10).values, color='skyblue')
plt.title('Top 10 Countries with the Highest Number of Netflix Titles')
plt.xlabel('Country')
plt.ylabel('Number of Titles')
plt.xticks(rotation=25)
plt.tight_layout()

#What are the top 10 directors featured on Netflix?
director_counts = df['director'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(director_counts.head(10).index, director_counts.head(10).values, color='salmon')
plt.title('Top 10 Directors On Netflix')
plt.ylabel("Movies")
plt.xticks(rotation=25)

#Plot a histogram showing distribution of Netflix titles by release year
plt.figure(figsize=(10, 6))
plt.hist(df['release_year'], bins=25, color='lightgreen', edgecolor='black')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.title('Distribution of Netflix Titles by Release Year')
plt.xticks(rotation=25)
plt.show()