import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
data = {
    "Movie": [
        "Avatar",
        "Titanic",
        "The Avengers",
        "Iron Man",
        "Interstellar",
        "The Dark Knight"
    ],
    "Genre": [
        "Action Adventure Sci-Fi",
        "Romance Drama",
        "Action Adventure Sci-Fi",
        "Action Sci-Fi",
        "Sci-Fi Drama",
        "Action Crime Drama"
    ]
}
df = pd.DataFrame(data)
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df["Genre"])
similarity = cosine_similarity(tfidf_matrix)
def recommend(movie):
    if movie not in df["Movie"].values:
        return "Movie not found"
    idx = df[df["Movie"] == movie].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    recommendations = [df["Movie"][i] for i, score in scores[1:3]]
    return recommendations
print("Recommended movies:", recommend("Avatar"))
