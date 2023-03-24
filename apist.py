import pandas as pd
import numpy as np
import streamlit as st
from surprise import Reader, Dataset, SVD




 # Leer el archivo Parquet
# Load data from parquet files
df1 = pd.read_parquet('./amazon.parquet')
df2 = pd.read_parquet('./netflix.parquet')
df3 = pd.read_parquet('./disney.parquet')
df4 = pd.read_parquet('./hulu.parquet')

# Create a Reader object to parse the data
reader = Reader(rating_scale=(0.5, 5))

# Load the data into a Surprise Dataset object
data1 = Dataset.load_from_df(df1[['userId', 'movieId', 'score_mean']], reader)
data2 = Dataset.load_from_df(df2[['userId', 'movieId', 'score_mean']], reader)
data3 = Dataset.load_from_df(df3[['userId', 'movieId', 'score_mean']], reader)
data4 = Dataset.load_from_df(df4[['userId', 'movieId', 'score_mean']], reader)

# Define an SVD model with 100 latent factors
model1 = SVD(n_factors=100)
model2 = SVD(n_factors=100)
model3 = SVD(n_factors=100)
model4 = SVD(n_factors=100)

# Train the models with the data
trainset1 = data1.build_full_trainset()
trainset2 = data2.build_full_trainset()
trainset3 = data3.build_full_trainset()
trainset4 = data4.build_full_trainset()

model1.fit(trainset1)
model2.fit(trainset2)
model3.fit(trainset3)
model4.fit(trainset4)


# Llama la función que has proporcionado
def get_movie_recommendations1(user_id):
    user_movies = df1[df1['userId'] == user_id]['movieId'].unique()
    user_unrated_movies = df1[~df1['movieId'].isin(user_movies)]['movieId'].unique()
    user_ratings = [(movie_id, model1.predict(user_id, movie_id).est) for movie_id in user_unrated_movies]
    user_ratings_sorted = sorted(user_ratings, key=lambda x: x[1], reverse=True)[:5]
    recommended_movies1 = df1[df1['movieId'].isin([movie[0] for movie in user_ratings_sorted])]['title'].unique()
    return recommended_movies1

def get_movie_recommendations2(user_id):
    user_movies = df2[df2['userId'] == user_id]['movieId'].unique()
    user_unrated_movies = df2[~df2['movieId'].isin(user_movies)]['movieId'].unique()
    user_ratings = [(movie_id, model2.predict(user_id, movie_id).est) for movie_id in user_unrated_movies]
    user_ratings_sorted = sorted(user_ratings, key=lambda x: x[1], reverse=True)[:5]
    recommended_movies2 = df2[df2['movieId'].isin([movie[0] for movie in user_ratings_sorted])]['title'].unique()
    return recommended_movies2

def get_movie_recommendations3(user_id):
    user_movies = df3[df3['userId'] == user_id]['movieId'].unique()
    user_unrated_movies = df3[~df3['movieId'].isin(user_movies)]['movieId'].unique()
    user_ratings = [(movie_id, model3.predict(user_id, movie_id).est) for movie_id in user_unrated_movies]
    user_ratings_sorted = sorted(user_ratings, key=lambda x: x[1], reverse=True)[:5]
    recommended_movies3 = df3[df3['movieId'].isin([movie[0] for movie in user_ratings_sorted])]['title'].unique()
    return recommended_movies3

def get_movie_recommendations4(user_id):
    user_movies = df4[df4['userId'] == user_id]['movieId'].unique()
    user_unrated_movies = df4[~df4['movieId'].isin(user_movies)]['movieId'].unique()
    user_ratings = [(movie_id, model4.predict(user_id, movie_id).est) for movie_id in user_unrated_movies]
    user_ratings_sorted = sorted(user_ratings, key=lambda x: x[1], reverse=True)[:5]
    recommended_movies4 = df4[df4['movieId'].isin([movie[0] for movie in user_ratings_sorted])]['title'].unique()
    return recommended_movies4


# Opciones de consulta


st.title("Recomendacion de Películas para ti")
st.image('https://cronicaglobal.elespanol.com/uploads/s1/11/08/49/61/logos-de-las-distintas-plataformas-de-streaming.jpeg',)
st.header('Encuentra las mejores recomendaciones de las mejores plataformas de streaming para ti segun tu usuario :sunglasses:')


# Crea la aplicación de Streamlit

st.title(" AMAZON PRIME VIDEO")
st.image('https://m.media-amazon.com/images/G/01/primevideo/seo/primevideo-seo-logo.png')
st.write("Introduce tu ID de usuario de Amazon:")
user_id = st.text_input("ID de Usuario Amazon", int())
if st.button('Obtener recomendaciones Amazon'):
    if not user_id:
            st.error("Por favor ingresa tu ID de usuario.")
    else:
        recommended_movies1 = get_movie_recommendations1(int(user_id))
        st.write("Las 5 películas recomendadas para el usuario {} son:".format(user_id))
        if len(recommended_movies1) == 0:
            st.error("No se encontraron recomendaciones para el usuario {}.".format(user_id))
        else:
            st.success("Las 5 películas recomendadas para el usuario {} son:".format(user_id))
        for i, movie in enumerate(recommended_movies1, start=1):
            st.write("{}. {}".format(i, movie))
       

st.title(" NETFLIX")
st.image('https://conocedores.com/wp-content/uploads/2016/06/netflixn.jpg')
st.write("Introduce tu ID de usuario de Netflix:")
user_id = st.text_input("ID de Usuario Netflix", int())
if st.button('Obtener recomendaciones Netflix'):
    if not user_id:
            st.error("Por favor ingresa tu ID de usuario.")
    else:
        recommended_movies2 = get_movie_recommendations2(int(user_id))
        st.write("Las 5 películas recomendadas para el usuario {} son:".format(user_id))
        if len(recommended_movies2) == 0:
            st.error("No se encontraron recomendaciones para el usuario {}.".format(user_id))
        else:
            st.success("Las 5 películas recomendadas para el usuario {} son:".format(user_id))
        for i, movie in enumerate(recommended_movies2, start=1):
            st.write("{}. {}".format(i, movie))
       


st.title(" DISNEY")
st.image('https://graffica.info/wp-content/uploads/2018/11/disneyplus-1200x675.jpg')
st.write("Introduce tu ID de usuario de Disney:")
user_id = st.text_input("ID de Usuario Disney", int())
if st.button('Obtener recomendaciones Disney'):
    if not user_id:
        st.error("Por favor ingresa tu ID de usuario.")
    else:
        recommended_movies3 = get_movie_recommendations3(int(user_id))
        st.write("Las 5 películas recomendadas para el usuario {} son:".format(user_id))
        if len(recommended_movies3) == 0:
            st.error("No se encontraron recomendaciones para el usuario {}.".format(user_id))
        else:
            st.success("Las 5 películas recomendadas para el usuario {} son:".format(user_id))
        for i, movie in enumerate(recommended_movies3, start=1):
            st.write("{}. {}".format(i, movie))
       


st.title(" HULU")
st.image('https://cloudfront-us-east-1.images.arcpublishing.com/infobae/4KLMKFUPNBBIPCWPKYIWORIBSA.png')
st.write("Introduce tu ID de usuario de Hulu:")
user_id = st.text_input("ID de Usuario Hulu", int())
if st.button('Obtener recomendaciones Hulu'):
    if not user_id:
        st.error("Por favor ingresa tu ID de usuario.")
    else:
        recommended_movies4 = get_movie_recommendations4(int(user_id))
        st.write("Las 5 películas recomendadas para el usuario {} son:".format(user_id))
        if len(recommended_movies4) == 0:
            st.error("No se encontraron recomendaciones para el usuario {}.".format(user_id))
        else:
            st.success("Las 5 películas recomendadas para el usuario {} son:".format(user_id))
        for i, movie in enumerate(recommended_movies4, start=1):
            st.write("{}. {}".format(i, movie))
       

