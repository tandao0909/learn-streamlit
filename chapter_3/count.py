import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./avocado.csv")
fig = plt.figure(figsize=(10, 5))
sns.countplot(x="year", data=df)
st.pyplot(fig)
