import streamlit as st
import Functions

def add_todo():
    todo = st.session_state["IT"] + '\n'
    todos.append(todo)
    Functions.write_t(todos)

todos = Functions.get_t()


st.title("To Do list")
st.subheader("Pattern your life")
st.write("This app is created to better your life")

remove = []

if todos is not None:
    for i, todo in enumerate(todos):
        checkbox = st.checkbox(todo, key=todo)
        if checkbox:
            remove.append(i)
            st.warning(f"Removing{remove}")


    for g in reversed(remove):
        todos.pop(g)

else:
    st.warning("issue reading file")

st.text_input(label="", placeholder="Add new task", on_change=add_todo, key="IT" )  # Label is part if this function




#link
# https://5titch-letssee-web-jjduun.streamlit.app/