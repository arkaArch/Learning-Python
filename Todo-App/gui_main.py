import modules.functions as fns
import FreeSimpleGUI as sg

todos_from_file = fns.get_todos_from_file()

layout = [[sg.Text("Type in a todo: ")],
          [sg.Input(key="to_do_input"), sg.Button("Add")],
          [sg.Listbox(values=[todo.strip("\n") for todo in todos_from_file],
                      key="todos",
                      enable_events=True,
                      size=(45, 10))],
          [sg.Button("Edit"), sg.Button("Complete"), sg.Push(), sg.Button("Exit")]]

window = sg.Window("Todo app",
                   layout,
                   font=("FiraCode Nerd Font", 12))

while True:
    event, value = window.read()

    # print("Event = ", event, ", Value = ", value)
    # - for "Add" it printed -> Event =  Add , Value =  {'to_do_input': 'what is written in input box'}
    # - for "Listbox" it printed -> Event =  todos , Value =  Value =  {'to_do_input': '', 'todos': ['Selected to-do']}
    # - for "Edit" it printed -> Event =  Edit , Value =  {'to_do_input': 'edited_todo', 'todos': ['Selected to-do']}
    # - for "Complete" it printed -> Event =  Complete , Value =  {'to_do_input': 'Selected to-do', 'todos': ['Selected to-do']}
    # - for "Exit" it printed -> Event =  Exit , Value =  {'to_do_input': '', 'todos': []}
    # - for sg.WINDOW_CLOSED it printed -> Event =  None , Value =  {'to_do_input': None, 'todos': None}
    match event:
        case "Add":
            if value["to_do_input"].strip() == "":
                sg.popup("Please write a todo before add",
                         font=("FiraCode Nerd Font", 12),
                         no_titlebar=True,
                         button_justification="center")
            else:
                todos_from_file.append(value["to_do_input"].strip() + "\n")
                fns.write_todos(todos_from_file)
                # - Update the window - specifically listbox(which has a key value of "to_do_input")
                # - with added to_do and before that strip the new lines before showing
                window["todos"].update(values=[todo.strip("\n") for todo in todos_from_file])
        case "Edit":
            try:  # If user press Edit without selecting a to-do
                selected_todo = value["todos"][0]  # [0] to get the string from the list 'todos': ['selected to_do']
                edited_todo = value["to_do_input"]
                # - Find the index of selected to-do
                index_of_selected_todo = todos_from_file.index(
                    selected_todo + "\n")  # Selected to-do is stripped with "\n"
                # - Replace the selected to-do with edited to-do
                todos_from_file[index_of_selected_todo] = edited_todo + "\n"
                # - Write the new todos
                fns.write_todos(todos_from_file)
                # - Update the list box with edited to_do with stripped new lines
                window["todos"].update(values=[todo.strip("\n") for todo in todos_from_file])
            except IndexError:
                sg.popup("Please select an item first",
                         font=("FiraCode Nerd Font", 12),
                         no_titlebar=True,
                         button_justification="center")
        case "todos":
            # - Update the input (which has a key value of "to_do_input")
            window["to_do_input"].update(value=value['todos'][0])
        case "Complete":
            try:
                selected_todo = value["todos"][0]
                # - Remove the selected to-do
                todos_from_file.remove(selected_todo + "\n")
                # - Write the new todos
                fns.write_todos(todos_from_file)
                # - Update the list box with edited to_do_input with stripped new lines
                window["todos"].update(values=[todo.strip("\n") for todo in todos_from_file])
                # - Also update the input box
                window["to_do_input"].update("")
            except IndexError:
                sg.popup("Please select an item first",
                         font=("FiraCode Nerd Font", 12),
                         no_titlebar=True,
                         button_justification="center")
        case "Exit" | sg.WINDOW_CLOSED:
            break

window.close()
