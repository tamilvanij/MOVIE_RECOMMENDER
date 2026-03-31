import pandas as pd

# Dummy ratings (simulate users)
ratings = pd.DataFrame({
    'userId': [1,1,1,2,2,3,3],
    'movieId': [1,2,3,1,4,2,5],
    'rating': [5,4,5,4,5,3,4]
})

def get_collab_recommendations(movie_id):
    similar_users = ratings[ratings['movieId'] == movie_id]['userId']

    rec_movies = ratings[
        (ratings['userId'].isin(similar_users)) &
        (ratings['movieId'] != movie_id)
    ]['movieId']

    return rec_movies.unique().tolist()