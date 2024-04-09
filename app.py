import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title and Overview
st.title('Boston Housing Dataset Analysis')
st.markdown("""
This app explores the Boston Housing dataset, providing insights into the housing values in suburbs of Boston, along with various features influencing the housing prices. Below is a brief overview of the dataset columns:

- `crim`: Per capita crime rate by town.
- `zn`: Proportion of residential land zoned for lots over 25,000 sq.ft.
- `indus`: Proportion of non-retail business acres per town.
- `chas`: Charles River dummy variable (1 if tract bounds river; 0 otherwise).
- `nox`: Nitrogen oxides concentration (parts per 10 million).
- `rm`: Average number of rooms per dwelling.
- `age`: Proportion of owner-occupied units built prior to 1940.
- `dis`: Weighted distances to five Boston employment centers.
- `rad`: Index of accessibility to radial highways.
- `tax`: Full-value property-tax rate per $10,000.
- `ptratio`: Pupil-teacher ratio by town.
- `b`: 1000(Bk - 0.63)^2 where Bk is the proportion of black residents by town.
- `lstat`: Percentage of lower status population.
- `medv`: Median value of owner-occupied homes in $1000's.
""")

# Function to load the dataset
@st.cache
def load_data():
    data = pd.read_csv('BostonHousing.csv')
    return data

df = load_data()

# Sidebar for filtering
st.sidebar.header('Filter Options')

# Slider for number of rooms (rm)
min_rooms, max_rooms = float(df['rm'].min()), float(df['rm'].max())
rooms = st.sidebar.slider('Number of Rooms (rm)', min_rooms, max_rooms, (min_rooms, max_rooms))

# Dropdown for CHAS (Charles River dummy variable)
chas_options = [0, 1]  # Assuming chas column is either 0 or 1
chas = st.sidebar.selectbox('Proximity to Charles River (chas)', options=chas_options)

# Multiselect for property tax rate (tax)
unique_tax_rates = sorted(df['tax'].unique().tolist())
selected_tax_rates = st.sidebar.multiselect('Property Tax Rate (tax)', options=unique_tax_rates, default=unique_tax_rates)

# Filter data based on selections
filtered_df = df[(df['rm'] >= rooms[0]) & (df['rm'] <= rooms[1]) & (df['chas'] == chas) & (df['tax'].isin(selected_tax_rates))]

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
