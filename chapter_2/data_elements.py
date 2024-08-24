import streamlit as st
import pandas as pd
import numpy as np

st.header("Render a dataframe")

df = pd.DataFrame(
    np.random.randn(30, 10), 
    columns=(f"col_no {i}" for i in range(10))
)
st.dataframe(df)

st.header("Highlight a dataframe")
st.dataframe(df.style.highlight_min(axis=0))

st.header("Render a table")
st.table(df)
