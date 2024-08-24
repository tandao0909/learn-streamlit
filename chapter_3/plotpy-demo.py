import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

data = pd.read_csv("avocado.csv")

st.header("Plotly Pie Chart")

pie_chart = go.Figure(
    go.Pie(
        labels = data.type,
        values = data.AveragePrice,
        hoverinfo = "label+percent",
        textinfo = "value+percent"
    )
)

st.plotly_chart(pie_chart)

st.header("Plotly Donut Chart")

donut_chart = px.pie(
        names = data.type,
        values = data.AveragePrice,
        hole = 0.25
)

st.plotly_chart(donut_chart)

st.header("Plotly Scatter Chart")

scatter_chart = px.scatter(
    x = data.Date,
    y = data.AveragePrice
)

st.plotly_chart(scatter_chart)


albania_df = data[data["region"]=="Albany"][data["year"]==2015]

st.header("Plotly Line Chart")

line_chart = px.line(
    x = albania_df["Date"],
    y = albania_df["Large Bags"]
)

st.plotly_chart(line_chart)

st.header("Plotly Bar Chart")

bar_chart = px.bar(
    albania_df,
    title="Bar Graph",
    x="Date",
    y="Large Bags"
)

st.plotly_chart(bar_chart)

st.header("Plotly Colorful Bar Chart")

bar_chart = px.bar(
    albania_df,
    title="Bar Graph",
    x="Date",
    y="Large Bags",
    color="Large Bags"
)

st.plotly_chart(bar_chart)

st.header("Plotly Colorful Horizontal Bar Chart")

bar_chart = px.bar(
    albania_df,
    title="Bar Graph",
    x="Large Bags",
    y="Date",
    color="Large Bags",
    orientation="h"
)

st.plotly_chart(bar_chart)
