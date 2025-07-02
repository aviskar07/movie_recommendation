import streamlit as st
import pickle
import pandas as pd
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    for item in movies_list:
        recommended_movies.append(movies.iloc[item[0]]['title'])
    return recommended_movies
movies_dict=pickle.load(open('movie_dict.pkl', 'rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl', 'rb'))
st.title("Movie Recommender")
selected_movie=st.selectbox('choose any one',movies['title'].values)
if st.button('recommend'):
    name=recommend(selected_movie)
    for i in name:
        st.write(i)
