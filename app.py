import streamlit as st
import numpy as np
import difflib
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_"
                 "key=cc963a2d8536615cfa65dd5244668a04&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie_name):
    movies_index = movies_list['title'].tolist()

    recommended_movies = difflib.get_close_matches(movie_name,movies_index)

    close_match = recommended_movies[0]

    index = movies_list[movies_list.title==close_match]['index'].values[0]

    score = list(enumerate(value[index]))

    sorted_movies = sorted(score,key = lambda x:x[1],reverse=True) [1:11]
    recommender_movies = []
    recommender_movies_posters= []
    for i in sorted_movies:
        movie_id = movies_list.iloc[i[0]].id
        recommender_movies.append(movies_list.iloc[i[0]].title)
        recommender_movies_posters.append(fetch_poster(movie_id))
    return recommender_movies,recommender_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies_list= pd.DataFrame(movies_dict)

value = pickle.load(open('similarity.pkl','rb'))
st.title("Movies Recommendation Engine")
selected_movie_name = st.selectbox(
     'How would you like to be contacted?',
     movies_list.title)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)

    col1,col2,col3,col4,col5,col6,col7,col8,col9,col10 = st.columns(10)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
    with col6:
        st.text(names[5])
        st.image(posters[5])
    with col7:
        st.text(names[6])
        st.image(posters[6])
    with col8:
        st.text(names[7])
        st.image(posters[7])
    with col9:
        st.text(names[8])
        st.image(posters[8])
    with col10:
        st.text(names[9])
        st.image(posters[9])
