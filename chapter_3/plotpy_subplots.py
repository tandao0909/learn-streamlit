import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

data = pd.read_csv("avocado.csv")

alabany_df = data[data["region"]=="Albany"][data["year"]==2015]

fig = make_subplots(rows=3, cols=1)

fig.add_trace(go.Scatter(
    x=alabany_df["Date"],
    y=alabany_df["Total Bags"]
), row=1, col=1)

fig.add_trace(go.Scatter(
    x=alabany_df["Date"],
    y=alabany_df["Small Bags"]
), row=2, col=1)

fig.add_trace(go.Scatter(
    x=alabany_df["Date"],
    y=alabany_df["Large Bags"]
), row=3, col=1)

st.plotly_chart(fig)