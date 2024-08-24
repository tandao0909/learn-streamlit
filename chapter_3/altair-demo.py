import altair as alt
import streamlit as st
import pandas as pd

df = pd.read_csv("albany.csv")

st.title("Altair Box Plot")

box_plot = alt.Chart(df).mark_boxplot().encode(
    x = "Date",
    y = "Large Bags"
)

st.altair_chart(box_plot)

st.title("Altair Area Chart")

area = alt.Chart(df).mark_area(color="orange").encode(
    x = "Date",
    y = "Large Bags"
)

st.altair_chart(area)

st.title("Altair Heatmap")

heat_map = alt.Chart(df).mark_rect().encode(
    alt.Y("AveragePrice:Q"),
    alt.X("Large Bags:Q"),
    alt.Color("AveragePrice:Q"),
    tooltip = ["AveragePrice", "type", "Large Bags", "Date"]
).interactive()

st.altair_chart(heat_map)
