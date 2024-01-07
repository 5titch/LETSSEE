import streamlit as st
import functions


todos = functions.get_t()

st.title("To Do list")
st.subheader("Pattern your life")
st.write("This app is created to better your life")



for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new task")  # Label is part if this function