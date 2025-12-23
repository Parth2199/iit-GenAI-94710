import streamlit as st

st.title("My first Streamlit Program")
st.header("Welcome to GenAI Training Programme!!")
st.write("Hello students, I hope you are enjoying tech stuff here...")

if st.button("Click Me!!", type="primary"):
    st.toast("You clicked me...") 