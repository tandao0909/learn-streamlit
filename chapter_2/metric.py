import streamlit as st

st.header("Basic metric")
st.metric(label="Temperature", value=" 31 °C", delta="1.2 °C")

st.header("Many metrics")
# Defining columns
c1, c2, c3 = st.columns(3)

c1.metric("Rainfall", "100 cm", "10 cm")

c2.metric(label="Population", value="123 billions", delta="1 billion", delta_color="inverse")

c3.metric(label="Customers", value=100, delta=10, delta_color="off")

st.metric(label="Speed", value=None, delta=0)

st.metric("Trees", "91456", "-1123649")