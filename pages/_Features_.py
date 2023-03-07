import streamlit as st
import pandas as pd
from main import upload
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

st.title("Data Description and Cleaning")

data = upload()
df  = pd.read_csv(data)    

@st.cache_data
def show_data(df):
    st.table(df.head())
def get_features_md(df):
    features = list(df.columns)
    md =""
    for i in features:
        md+= "* "+i.replace("_" ," ").title()+" \n"
    return md
def numerical_features_list(df):
    return df.select_dtypes(include=np.number).columns.tolist()

def sns_distplot(df, feature,x=10,y=5):
    fig = plt.figure(figsize=(x,y))
    sns.displot(x= df[feature])
    st.pyplot(fig)

def plotly_distplot(df, feature):
    plot =px.histogram(df ,x= feature)
    st.plotly_chart(plot)
    
    




st.subheader("Your Data:")
show_data(df)
st.subheader("Features :")
st.markdown(get_features_md(df))
st.subheader("Numerical Features :")
numerical_features = numerical_features_list(df)

sns_distplot(df,"Age")
plotly_distplot(df,"Age")




