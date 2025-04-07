import pandas as pd
from analysis_app.models import Media

netflix_data = r'../netflix_titles_cleaned.csv'
df = pd.read_csv(netflix_data)
print(df.columns)
df['date_added'] = df['date_added'].str.strip()  # Clean spaces
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce', format='%B %d, %Y')

for index, row in df.iterrows():
    media = Media(
        type=row['type'],
        title=row['title'],
        director=row['director'],
        cast=row['cast'],
        country=row['country'],
        date_added=row['date_added'],
        release_year=row['release_year'],
        rating=row['rating'],
        duration=row['duration'],
        listed_in=row['listed_in'],
        description=row['description']
    )
    media.save()

print("CSV data has been loaded into the Django database.")