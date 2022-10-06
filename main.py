import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st

# # settings for all of the pages in the app
st.set_page_config(layout="wide")

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# setting plot color themes
sns.set_theme(style="white", palette=sns.color_palette("Set2"))

def artist_overview():
    pass

def mainstay_eda():
    pass

def modelling():
    pass

def recommender_engine():
    pass

def playlists():
    pass

def the_team():
    pass

list_of_pages = [
    "Artist Overview",
    "Mainstay OPM",
    "Modelling",
    "Recommender Engine",
    "Playlists",
    "The Team"
]

st.sidebar.title(':scroll: Main Pages')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Artist Overview":
    artist_overview()

elif selection == "Mainstay OPM":
    mainstay_eda()

elif selection == "Modelling":
    modelling()

elif selection == "Recommender Engine":
    recommender_engine()

elif selection == "Playlists":
    playlists()

elif selection == "The Team":
    the_team()