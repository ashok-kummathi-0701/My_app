import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello, Streamlit!")


st.subheader("st.column")
with st.sidebar:
    st.header("About app")
    st.write("This is my first app!")

st.header("This is a simple Streamlit app.", divider="rainbow")
st.markdown("This is created by using st.markdown")
col1, col2 = st.columns(2)
with col1:
    x = st.slider("Choose an x value",1,10)
with col2:
    st.write("The value of :blue[**x**] is", x)

st.subheader("st.area_chart")

df = pd.DataFrame(np.random.standard_normal((20, 3)), columns=["a", "b", "c"])

st.area_chart(df)
