import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import joblib

# Załaduj dane z pliku CSV
df = pd.read_csv('movies.csv')

# Użyj tylko kolumn 'title', 'genre', 'year', 'rating' (zakładam, że kolumna 'overview' jest opisana jako 'genre')
df = df[['Movie','LeadStudio','RottenTomatoes','AudienceScore','Story','Genre','Year']].dropna()

# Utwórz model TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['Genre'])

# Oblicz macierz podobieństwa
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Zapisz model i dane do pliku
joblib.dump((df, cosine_sim), 'movie_recommender_model.pkl')

print("Model wytrenowany i zapisany jako 'movie_recommender_model.pkl'")
