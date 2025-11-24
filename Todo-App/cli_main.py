from time import strftime
from modules.functions import get_todos_from_file, write_todos

now = strftime("%b %d, %Y %I:%M%p")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        # Read from todos.txt to check for existing todos
        todos = get_todos_from_file()
        todo = user_action[4:]   # Get the text after 'add '
        # Get the new todos from user and append them to the list
        todos.append(todo + "\n")

        # Write the new list into the file
        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos_from_file()

        for index, item in enumerate(todos, start=1):
            item = item.strip('\n')
            print(f"{index}. {item.capitalize()}")

    elif user_action.startswith("edit"):
        try:
            todo_number = int(user_action[5:])    # Get the text after 'edit '
            todos = get_todos_from_file()

            # Modify the todo_ list
            new_todo = input("Enter the new todo: ")
            todos[todo_number - 1] = new_todo + "\n"

            # Write the todos into the file
            write_todos(todos)
        except ValueError:
            print("Please enter a todo number after edit.")

    elif user_action.startswith("complete"):
        try:
            todo_number = int(user_action[9:])    # Get the text after 'complete '
            # Read the todos from file
            todos = get_todos_from_file()

            # Remove completed todo_ from todos list
            todos.pop(todo_number - 1)

            # Write the modified todos into the file
            write_todos(todos)
        except ValueError:
            print("Please enter a todo number after complete.")
        except IndexError:
            print("You do not have that many todos")

    elif user_action.startswith("exit"):
        break

    else:
        print("You entered an unknown command")