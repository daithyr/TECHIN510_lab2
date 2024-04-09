import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston

# Load Boston housing data
@st.cache
def load_data():
    boston = load_boston()
    data = pd.DataFrame(boston.data, columns=boston.feature_names)
    data['MEDV'] = boston.target
    return data

df = load_data()

# Sidebar for filtering
st.sidebar.header('Filter Options')

# Slider for number of rooms
rooms = st.sidebar.slider('Number of Rooms (RM)', float(df['RM'].min()), float(df['RM'].max()), (float(df['RM'].min()), float(df['RM'].max())))

# Filtering data based on selection
filtered_df = df[(df['RM'] >= rooms[0]) & (df['RM'] <= rooms[1])]

# Main panel

# Use columns for layout
col1, col2 = st.columns(2)

with col1:
    st.header("Distribution of Property Prices")
    fig, ax = plt.subplots()
    sns.histplot(filtered_df['MEDV'], bins=30, kde=True, ax=ax)
    st.pyplot(fig)

with col2:
    st.header("Correlation Heatmap")
    # Compute correlation matrix
    corr = filtered_df.corr()
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))
    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})
    st.pyplot(f)

# Assuming augmented data with 'LAT' and 'LON' for map visualization
# If you don't have this data, comment out this section
if 'LAT' in df.columns and 'LON' in df.columns:
    st.header("Map of Properties")
    st.map(filtered_df[['LAT', 'LON']])

# This is a placeholder. If you don't have latitude and longitude data,
# you might not be able to use this part directly.
