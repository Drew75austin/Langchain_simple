import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns   
import seaborn.objects as so



# from langchain.prompts import PromptTemplate
# from langchain.llms import OpenAI
# from langchain.chains import LLMChain


# Load the data into a data frame
Military_Data = pd.read_csv("military.csv") 

fig, ax = plt.subplots(figsize=(20,10))
st.write(sns.scatterplot(x="Military_Spending_Billion_USD", y="GDP_Trillion_USD", size="Population_Millions",
            sizes=(40, 400), alpha=.5, palette="muted", data=Military_Data))


st.pyplot(fig)


# llm = OpenAI(temperature=0.9)

# prompt_template = "What is a good name for a company that makes {product}?"
# llm = OpenAI(temperature=0)
# llm_chain = LLMChain(
#     llm=llm,
#     prompt=PromptTemplate.from_template(prompt_template)
# )


# prodcut = st.text_input("What prodcut type do you want to find a good company name for?", '')
# st.write(llm_chain(prodcut))



