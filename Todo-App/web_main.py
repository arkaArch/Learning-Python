import streamlit as st
import modules.functions as fns

todos = fns.get_todos_from_file()

st.title("Todo App ")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")