import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns   
import seaborn.objects as so
import plotly.express as px

Military_Data = pd.read_csv("military.csv") 

fig, ax = plt.subplots(figsize=(20,10))
st.write(sns.scatterplot(x="Military_Spending_Billion_USD", y="GDP_Trillion_USD", size="Population_Millions",
            sizes=(40, 400), alpha=.5, palette="muted", data=Military_Data))
st.pyplot(fig)


# Sample data
data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 15, 13, 17, 20],
    'category': ['A', 'B', 'A', 'C', 'B']
})

# Create a scatter plot using Plotly Express
fig = px.scatter(data, x='x', y='y', color='category', title='Scatter Plot with Categories')

# Display the Plotly scatter plot in the Streamlit app
st.plotly_chart(fig)


