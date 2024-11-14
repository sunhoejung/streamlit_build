import pandas as pd
import streamlit as st

@st.cache_data
def call_data():
    data = pd.read_csv("data/seoul_estate.csv")

    return data