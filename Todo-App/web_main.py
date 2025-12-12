import streamlit as st
import modules.functions as fns

# You can deploy this app by create a new project with pycharm and build only streamlit app ( i.e. web_main.py with
# ofcourse function.py, todos.txt and requirements.txt) and upload the project into github and deploy to streamlit
# community from the "Deploy" button in the streamlit app in your browser.

todos = fns.get_todos_from_file()

def add_todo():
    todo_to_be_added = st.session_state["new_todo"]
    todos.append(todo_to_be_added + "\n")
    fns.write_todos(todos)


st.title("Todo App ")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    # Check if a checkbox is checked
    if checkbox:
        # Remove the checked to-do from todos list
        todos.pop(index)
        # Write the updated todos in the file
        fns.write_todos(todos)
        # Also delete the to-do from the session state
        del st.session_state[todo]
        # Rerun the entire streamlit app
        st.rerun()

st.text_input(label=" ",
              placeholder="Add new todo...",
              on_change=add_todo,
              key="new_todo")   # We use key for session_state