import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):

    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))

    data=response.json()

    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
   
    recommended_movies =[]

    recommended_movies_poster=[]
    for i in distances[1:6]:
        movie_id =movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        #fetch_poster from api
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster


movies_list= pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_list)

similarity = pickle.load(open('similarity.pkl','rb'))


st.set_page_config(page_title="Background Image App")

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVU0pviDKJOH2M0GLJz2Ld4NWUnkPsqpZtBA&s");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)





st.title('Movie Recomended System')
Selected_movie_name=st.selectbox(
    'how would you like to be selected a movie',

    movies['title'].values
)
if st.button('Recommend'):
    names,posters = recommend(Selected_movie_name)
    #st.write(Selected_movie_name)

    col1,col2,col3,col4,col5,=st.columns(5)

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