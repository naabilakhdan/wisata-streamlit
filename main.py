 # Importing modules
import pickle # For loading model
import streamlit as st # For web app
import os
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


#page config
st.set_page_config(
    page_title="BANDUNG WISATA",
    page_icon="images/logo.png",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Mendapatkan path ke folder data
data_folder = os.path.join(os.path.dirname(__file__), 'data')

# Membangun path ke file pickle
df_path = os.path.join(data_folder, 'df.pkl')
result_tfidf_path = os.path.join(data_folder, 'resulttfidf_wisata.pkl')
vector_tfidf_path = os.path.join(data_folder, 'vector_tfidf.pkl')

# Loading data frame
try:
    rec_wisata = pickle.load(open(df_path, 'rb'))
    result_tfidf = pickle.load(open(result_tfidf_path, 'rb'))
    vector_tfidf = pickle.load(open(vector_tfidf_path, 'rb'))
except FileNotFoundError:
    st.error("File not found. Make sure the pickle files are in the correct directory.")
except Exception as e:
    st.error(f"Error loading pickle files: {e}")

# Main heading
# st.image("images/logobalinest.png")
st.title('REKOMENDASI WISATA DI BANDUNG')

test = st.text_input('Input keyword tempat wisata yang ingin Anda kunjungi :')

    
def recommend(data):
    test_arr = vector_tfidf.transform([data])
    test_arr = test_arr.toarray()
    result = {}
    for id, vector in enumerate(result_tfidf):
        cosine_val = cosine_similarity([result_tfidf[id]], test_arr)
        result[id] = cosine_val

    result_desc = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
    recommended_image = []
    recommended_place_name = []
    recommended_city = []
    recommended_description = []
    recommended_price = []
    for n, place_id in enumerate(result_desc):
        if n > 5:
            break
        recommended_image.append(rec_wisata.loc[place_id,'image'])
        recommended_place_name.append(rec_wisata.loc[place_id, 'place_name'])
        recommended_city.append(rec_wisata.loc[place_id, 'city'])
        recommended_description.append(rec_wisata.loc[place_id, 'description'])
        recommended_price.append(rec_wisata.loc[place_id, 'price'])


    return recommended_image, recommended_place_name, recommended_city, recommended_description, recommended_price


if st.button('Tampilkan Rekomendasi'):
    recommended_image, recommended_place_name, recommended_city, recommended_description, recommended_price = recommend(test)

    #display with the columns
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(recommended_image[0], width=200, caption=recommended_place_name[0])
        with col2:
            st.subheader(recommended_place_name[0])
            with st.expander("Lokasi Wisata"):
                st.write(recommended_city[0])
            with st.expander("Deskripsi"):
                st.write(recommended_description[0])
            with st.expander("Harga Tiket Masuk"):
                st.write(recommended_price[0])

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(recommended_image[1], width=200, caption=recommended_place_name[1])
        with col2:
            st.subheader(recommended_place_name[1])
            with st.expander("Lokasi Wisata"):
                st.write(recommended_city[1])
            with st.expander("Deskripsi"):
                st.write(recommended_description[1])
            with st.expander("Harga Tiket Masuk"):
                st.write(recommended_price[1])

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(recommended_image[2], width=200, caption=recommended_place_name[2])
        with col2:
            st.subheader(recommended_place_name[2])
            with st.expander("Lokasi Wisata"):
                st.write(recommended_city[2])
            with st.expander("Deskripsi"):
                st.write(recommended_description[2])
            with st.expander("Harga Tiket Masuk"):
                st.write(recommended_price[2])

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(recommended_image[3], width=200, caption=recommended_place_name[3])
        with col2:
            st.subheader(recommended_place_name[3])
            with st.expander("Lokasi Wisata"):
                st.write(recommended_city[3])
            with st.expander("Deskripsi"):
                st.write(recommended_description[3])
            with st.expander("Harga Tiket Masuk"):
                st.write(recommended_price[3])

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(recommended_image[4], width=200, caption=recommended_place_name[4])
        with col2:
            st.subheader(recommended_place_name[4])
            with st.expander("Lokasi Wisata"):
                st.write(recommended_city[4])
            with st.expander("Deskripsi"):
                st.write(recommended_description[4])
            with st.expander("Harga Tiket Masuk"):
                st.write(recommended_price[5])