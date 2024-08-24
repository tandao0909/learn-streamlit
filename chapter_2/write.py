import streamlit as st
import pandas as pd

st.write(pd.DataFrame({
    "column one": [1, 2, 3, 4],
    "column two": [5, 6, 7, 8]
}
))

df = pd.DataFrame()