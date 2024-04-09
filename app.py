import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Function to load the dataset
@st.cache
def load_data():
    data = pd.read_csv('BostonHousing.csv')
    return data

df = load_data()

# Sidebar for filtering
st.sidebar.header('Filter Options')

# Slider for number of rooms (rm)
min_rooms, max_rooms = int(df['rm'].min()), int(df['rm'].max())
rooms = st.sidebar.slider('Number of Rooms (rm)', min_rooms, max_rooms, (min_rooms, max_rooms))

# Dropdown for CHAS (Charles River dummy variable)
chas_options = df['chas'].unique().tolist()
chas = st.sidebar.selectbox('Proximity to Charles River (chas)', chas_options)

# Filter data based on selections
filtered_df = df[(df['rm'] >= rooms[0]) & (df['rm'] <= rooms[1]) & (df['chas'] == chas)]

# Main panel with columns for layout
col1, col2 = st.columns(2)

with col1:
    st.header("Price Distribution")
    fig, ax = plt.subplots()
    sns.histplot(filtered_df['medv'], bins=20, kde=True, ax=ax)
    st.pyplot(fig)

with col2:
    st.header("Rooms vs. Price")
    fig, ax = plt.subplots()
    sns.scatterplot(x='rm', y='medv', data=filtered_df, ax=ax)
    ax.set_xlabel('Number of Rooms')
    ax.set_ylabel('Median Value ($1000s)')
    st.pyplot(fig)

# Assuming additional visualizations or interactive elements might be added below
