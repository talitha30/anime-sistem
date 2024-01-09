import streamlit as st 
import numpy as np
import pandas as pd

df = pd.read_csv("animes_list.csv")
doc_sim_df = pd.read_csv("similarity.csv")

animes_list = df['title'].values
#st.write(animes_list.shape)

def anime_recommender(anime_title, animes=animes_list, doc_sims=doc_sim_df):
    # find movie id
    #st.write(anime_title)
    anime_idx = np.where(animes == anime_title)[0][0]
    # get movie similarities
    anime_similarities = doc_sims.iloc[anime_idx].values
    # get top 5 similar movie IDs
    similar_anime_idxs = np.argsort(-anime_similarities)[1:6]
    # get top 5 movies
    similar_animes = animes[similar_anime_idxs]
    # return the top 5 movies
    return similar_animes

st.title('Sistem Rekomendasi ')
st.header('Menggunakan Algoritma Tf-Idf dan Cosine Similarity', divider='blue')

inputss = st.text_input('Judul Anime', placeholder='Masukan')

if 'output' not in st.session_state:
    st.session_state.output = ''

def btn_action():
    try:
        st.session_state.output = anime_recommender(inputss, animes_list, doc_sim_df)
    except:
        st.session_state.output = "data tidak ditemukan"


submit_button = st.button('Submit', on_click=btn_action)

if submit_button:
    st.write("Berikut ini adalah rekomendasi anime:", st.session_state.output)
# st.button('submit', on_click=btn_action)
# st.write(st.session_state.output)
