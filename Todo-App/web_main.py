from linecache import clearcache

import streamlit as st
import modules.functions as fns

todos = fns.get_todos_from_file()

def add_todo():
    todo_to_be_added = st.session_state["new_todo"]
    todos.append(todo_to_be_added + "\n")
    fns.write_todos(todos)


st.title("Todo App ")

for todo in todos:
    st.checkbox(todo)

st.text_input(label=" ",
              placeholder="Add new todo...",
              on_change=add_todo,
              key="new_todo")