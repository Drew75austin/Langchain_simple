import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns   
import seaborn.objects as so
import plotly.express as px

data = pd.read_csv("military.csv") 

fig, ax = plt.subplots(figsize=(20,10))
st.write(sns.scatterplot(x="Military_Spending_Billion_USD", y="GDP_Trillion_USD", size="Population_Millions",
            sizes=(40, 400), alpha=.5, palette="muted", data=data))
st.pyplot(fig)

# Create a scatter plot using Plotly Express
fig = px.scatter(
    data,
    x='Military_Spending_Billion_USD',
    y='GDP_Trillion_USD',
    size='Population_Millions',
    text='Country',
    title='Military Spending vs. GDP with Population Size'
)

# Display the Plotly scatter plot in the Streamlit app directly
st.plotly_chart(fig)



