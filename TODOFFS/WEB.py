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

checkbox_states = st.session_state.get("checkbox_states", {})

# if todos is not None:
#     for i, toodo in enumerate(todos):
#         checkbox = st.checkbox(toodo, key=todo)
#         if checkbox:
#             remove.append(i)
#             st.warning(f"removing {toodo} and {i}")
#     if remove:
#         st.warning(f"Removing{remove}")
#     for g in reversed(remove):
#        todos.pop(g)

for i, todo in enumerate(todos):
    checkbox_states[i] = st.checkbox(todo, key=f"checkbox_{i}", value=checkbox_states.get(i, False))    # get method goes hand in hand with keys
    print(checkbox_states)



# removal
remove_indices = [i for i, state in checkbox_states.items() if state]
if remove_indices:
    st.warning(f"{todo}, has been removed")
    todos = [todo for i, todo in enumerate(todos) if i not in remove_indices]
    Functions.write_t(todos)

for i in remove_indices:
    checkbox_states[i] = False

st.session_state.checkbox_states = checkbox_states

st.text_input(label="", placeholder="Add new task", on_change=add_todo, key="IT" )  # Label is part if this function



#link
# https://5titch-letssee-web-jjduun.streamlit.app/