import streamlit as st
import ast
import operator
import math

st.markdown(
    """
    <h1 style='text-align: right; color: orange;'>
    Calculator 💸
    </h1>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("Calculators 🏦")

calculator = st.sidebar.selectbox(
    "Choose Calculator",
    ["Financial", "Simple", "Scientific"]
)

