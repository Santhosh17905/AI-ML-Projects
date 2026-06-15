import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD

movies = pd.read_csv(
    "movies.dat",
    sep="::",
    engine="python",
    encoding="latin-1",
    names=["movieId","title","genres"]
)

ratings = pd.read_csv(
    "ratings.dat",
    sep="::",
    engine="python",
    encoding="latin-1",
    names=["userId","movieId","rating","timestamp"]
)

rating_matrix = ratings.pivot_table(
    index="movieId",
    columns="userId",
    values="rating"
).fillna(0)

svd = TruncatedSVD(n_components=50)
matrix = svd.fit_transform(rating_matrix)
corr = np.corrcoef(matrix)

# ✅ Updated function
def recommend(movie_title, top_n=5):
    movie_match = movies[movies["title"].str.contains(movie_title, case=False)]

    if movie_match.empty:
        return []

    movie_index = movie_match.index[0]

    similarity_scores = list(enumerate(corr[movie_index]))
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )[1:top_n+1]

    results = []
    for i in similarity_scores:
        movie_title = movies.iloc[i[0]].title
        predicted_rating = round(i[1] * 5, 2)
        results.append({
            "title": movie_title,
            "rating": predicted_rating
        })

    return results