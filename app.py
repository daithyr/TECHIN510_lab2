import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'path/to/your/BostonHousing.csv'  # Update this to your actual file path
df = pd.read_csv(file_path)

# App title and dataset overview
st.title('Boston Housing Dataset Analysis')
st.markdown('''
This app provides analysis and visualization of the Boston Housing dataset.
Explore the relationship between various factors and median home values in Boston.
''')

# Sidebar for filtering
st.sidebar.header('Filter Options')
lstat_max = df['lstat'].max()
lstat_min = df['lstat'].min()
lstat_value = st.sidebar.slider('Lower status of the population (%)', float(lstat_min), float(lstat_max), (lstat_min, lstat_max))

# Filter data based on selection
filtered_data = df[df['lstat'].between(*lstat_value)]

# Distribution of Median Home Values
st.header('Distribution of Median Home Values')
fig, ax = plt.subplots()
sns.histplot(filtered_data['medv'], bins=20, kde=True, ax=ax)
st.pyplot(fig)

# Scatter Plot of RM vs. MEDV
st.header('Average Number of Rooms vs. Median Home Value')
fig, ax = plt.subplots()
sns.scatterplot(data=filtered_data, x='rm', y='medv', ax=ax)
ax.set_xlabel('Average Number of Rooms per Dwelling (RM)')
ax.set_ylabel('Median Value of Owner-Occupied Homes (MEDV)')
st.pyplot(fig)
