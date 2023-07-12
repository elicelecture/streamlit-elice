import streamlit as st
import pandas as pd
from streamlit_folium import folium_static
import folium
from folium.plugins import MarkerCluster

st.title("제주도에서 가장 핫한 곳은?")

df = pd.read_csv("jeju_place.csv")

m = folium.Map([sum(df["위도"])/len(df["위도"]),sum(df["경도"])/len(df["경도"])],zoom_start=9)
marker_cluster = MarkerCluster().add_to(m)

for i, j in zip(df["위도"],df["경도"]):
    folium.CircleMarker(
        [i,j]
    ).add_to(marker_cluster)

folium_static(m)