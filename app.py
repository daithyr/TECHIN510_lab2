import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to load the dataset
@st.cache
def load_data():
    data = pd.read_csv('BostonHousing.csv')
    return data

df = load_data()

# Sidebar for filtering
st.sidebar.header('Filter Options')

# Slider for number of rooms (RM)
min_rooms, max_rooms = int(df['RM'].min()), int(df['RM'].max())
rooms = st.sidebar.slider('Number of Rooms (RM)', min_rooms, max_rooms, (min_rooms, max_rooms))

# Dropdown for CHAS (Charles River dummy variable)
chas_options = df['CHAS'].unique().tolist()
chas = st.sidebar.selectbox('Proximity to Charles River (CHAS)', chas_options)

# Filter data based on selections
filtered_df = df[(df['RM'] >= rooms[0]) & (df['RM'] <= rooms[1]) & (df['CHAS'] == chas)]

# Main panel with columns for layout
col1, col2 = st.columns(2)

with col1:
    st.header("Price Distribution")
    fig, ax = plt.subplots()
    sns.histplot(filtered_df['MEDV'], bins=20, kde=True, ax=ax)
    st.pyplot(fig)

with col2:
    st.header("Rooms vs. Price")
    fig, ax = plt.subplots()
    sns.scatterplot(x='RM', y='MEDV', data=filtered_df, ax=ax)
    ax.set_xlabel('Number of Rooms')
    ax.set_ylabel('Median Value ($1000s)')
    st.pyplot(fig)

# Assuming you might want to add more visualization or interactive elements below
