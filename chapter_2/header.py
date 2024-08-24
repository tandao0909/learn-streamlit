import streamlit as st

st.write("This is write function")
st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")
st.caption("This is a caption")
st.text("This is a text")

st.markdown("# Hi")
st.markdown("**Bold text**")
st.markdown("*Italic text*")

st.latex(r"""
    \frac{\partial u}{\partial t} = \frac{\partial u}{\partial x} . \frac{\partial x}{\partial t}
""")
