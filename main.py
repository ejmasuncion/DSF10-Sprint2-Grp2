from os import read
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st

from Data_viz.final_data_viz import *

# # settings for all of the pages in the app
st.set_page_config(layout="wide")

def read_chartsdf():
    # read and process the charts dataset
    charts_df = pd.read_csv('data/spotify_daily_charts.csv')
    # transform date column into a datetime column
    charts_df['date'] = pd.to_datetime(charts_df['date'])

    return charts_df

def read_tracksdf():
    tracks_df = pd.read_csv('data/spotify_daily_charts_tracks.csv')
    return tracks_df

def read_zoodf():
    zoo_df=pd.read_csv("data_sp/zoo_tracks_data.csv")
    return zoo_df

def read_mainstaydf():
    mainstay_df=pd.read_csv("data_sp/tracks_data.csv")
    return mainstay_df

def read_streamsdf(charts_df = read_chartsdf(), tracks_df = read_tracksdf()):
    streams_df = charts_df.merge(tracks_df, on='track_id', how='left')
    streams_df = streams_df.drop(columns='track_name_y')
    streams_df = streams_df.rename(columns={'track_name_x': 'track_name'})
    streams_df['date']=pd.to_datetime(streams_df['date'])
    streams_df.set_index("date", inplace=True)
    
    return streams_df

def read_streams_df_opm(streams_df = read_streamsdf()):
    artists_df = pd.read_csv('data/spotify_daily_charts_artists_edited.csv')
    artists_df["OPM"]=np.where(artists_df.genres.str.contains('opm'),1,0)

    streams_df_opm=pd.merge(streams_df.reset_index(),artists_df[["artist_id","OPM"]], on="artist_id", how="left")
    streams_df_opm.set_index("date")
    streams_df_opm=streams_df_opm[streams_df_opm.OPM==1]
    streams_df_opm.set_index('date',inplace=True)

    return streams_df_opm

sns.set_theme(style="white", palette=sns.color_palette("Set2"))

def artist_overview():
    st.pyplot(plot_4charts("I Belong to the Zoo", read_streamsdf()))
    st.pyplot(plot_2boxcharts(read_zoodf()))
    st.pyplot(plot_6boxcharts(read_tracksdf(), read_mainstaydf()))
    st.pyplot(plot_market_eda(read_tracksdf(),read_streams_df_opm()))
    st.pyplot(plot_marketing_strat("I Belong to the Zoo",13, 1.3, read_streamsdf()))


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