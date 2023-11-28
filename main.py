 # Importing modules
import pickle # For loading model
import streamlit as st # For web app
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

# Loading data frame
rec_wisata = pickle.load(open('df.pkl','rb'))
result_tfidf = pickle.load(open('resulttfidf_wisata.pkl','rb'))
vector_tfidf = pickle.load(open('vector_tfidf.pkl','rb'))
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
    recommended_weekend = []
    recommended_weekday = []
    for n, place_id in enumerate(result_desc):
        if n > 4:
            break
        recommended_image.append(rec_wisata.loc[place_id,'image'])
        recommended_place_name.append(rec_wisata.loc[place_id, 'place_name'])
        recommended_city.append(rec_wisata.loc[place_id, 'city'])
        recommended_description.append(rec_wisata.loc[place_id, 'description'])
        recommended_weekend.append(rec_wisata.loc[place_id, 'weekend_price'])
        recommended_weekday.append(rec_wisata.loc[place_id, 'weekday_price'])

    return recommended_image, recommended_place_name, recommended_city, recommended_description, recommended_weekend, recommended_weekday


if st.button('Tampilkan Rekomendasi'):
    recommended_image, recommended_place_name, recommended_city, recommended_description, recommended_weekend, recommended_weekday = recommend(test)

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
            with st.expander("Tiket Saat Weekend"):
                st.write(recommended_weekend[0])
            with st.expander("Tiket Saat Weekday"):
                st.write(recommended_weekday[0])

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
            with st.expander("Tiket Saat Weekend"):
                st.write(recommended_weekend[1])
            with st.expander("Tiket Saat Weekday"):
                st.write(recommended_weekday[1])

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
            with st.expander("Tiket Saat Weekend"):
                st.write(recommended_weekend[2])
            with st.expander("Tiket Saat Weekday"):
                st.write(recommended_weekday[2])

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
            with st.expander("Tiket Saat Weekend"):
                st.write(recommended_weekend[3])
            with st.expander("Tiket Saat Weekday"):
                st.write(recommended_weekday[3])

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
            with st.expander("Tiket Saat Weekend"):
                st.write(recommended_weekend[4])
            with st.expander("Tiket Saat Weekday"):
                st.write(recommended_weekday[4])