import streamlit as st
import pandas as pd
import pickle

movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)

st.title("Movie Recommendation System")

similarity=pickle.load(open('similarity.pkl','rb'))


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
selected_movie_name=st.selectbox(
'which movie you want to see?',
movies['title'].values)

if st.button('Recommend'):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
