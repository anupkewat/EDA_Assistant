
import streamlit as st
import pandas as pd



#title
x= "Welcome :confetti_ball:"
st.title(x)
welcome_info = "<welcome info>"
st.write(welcome_info)

data = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

if data is not None:
    @st.cache_data
    def upload():
        uploaded_file = data
        return uploaded_file
        
