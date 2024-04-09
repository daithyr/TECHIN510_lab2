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

# Slider for the number of rooms (rm)
rooms = st.sidebar.slider('Number of Rooms (rm)', float(df['rm'].min()), float(df['rm'].max()), (float(df['rm'].min()), float(df['rm'].max())))

# Dropdown for CHAS (Charles River dummy variable)
chas = st.sidebar.selectbox('Proximity to Charles River (chas)', options=df['chas'].unique())

# Multiselect for RAD (index of accessibility to radial highways)
selected_rad = st.sidebar.multiselect('Accessibility to Radial Highways (rad)', options=df['rad'].unique(), default=df['rad'].unique())

# Filtering the dataframe
filtered_df = df[(df['rm'] >= rooms[0]) & (df['rm'] <= rooms[1]) & (df['chas'] == chas) & (df['rad'].isin(selected_rad))]

# Displaying the filtered dataframe
st.header('Filtered Data')
st.write(filtered_df)


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
