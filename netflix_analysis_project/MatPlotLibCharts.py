import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset into a Pandas DataFrame.
df = pd.read_csv('netflix_titles.csv')

# Charts work better with original data set, otherwise the filled, unknown fields dominate the charts.

country_counts = df['country'].value_counts()
plt.figure(figsize=(10, 6))
country_counts.head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 Countries with the Highest Number of Netflix Titles')
plt.xlabel('Country')
plt.ylabel('Number of Titles')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
