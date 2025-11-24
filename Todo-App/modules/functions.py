FILEPATH = "todos.txt"

def get_todos_from_file(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items """
    with open(filepath, "r") as file:
        todo_list = file.readlines()
        return todo_list


def write_todos(todo_list, filepath=FILEPATH):
    # You should write non-default parameter before
    """ Write the to-do items list in a text file """
    with open(filepath, 'w') as file:
        file.writelines(todo_list)
