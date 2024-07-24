import streamlit as st
import time
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""  # Clear the input field

st.title("My To Do App")
st.subheader(time.strftime("%b %d, %Y %H:%M"))

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{index}.{todo}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"{index}.{todo}"]
        st.rerun()

st.text_input(label=" ",
              key = "new_todo",
              placeholder="Add a new to do...",
              on_change=add_todo)

