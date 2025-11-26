import modules.functions as fns
import FreeSimpleGUI as sg

todos_from_file = fns.get_todos_from_file()

layout = [[sg.Text("Type in a todo: ")],
          [sg.Input(key="to_do"), sg.Button("Add")],
          [sg.Listbox(values=[todo.strip("\n") for todo in todos_from_file], key="todos", enable_events=True, size=(45, 10))],
          [sg.Button("Edit")]]

window = sg.Window("Todo app",
                   layout,
                   font=("FiraCode Nerd Font", 12))

while True:
    event, value = window.read()
    print("Event = ", event, ", Value = ", value)
    #- for "Add" it printed -> Event =  Add , Value =  {'to_do': 'what is written in input box'}
    #- for "Listbox" it printed -> Event =  todos , Value =  Value =  {'to_do': '', 'todos': ['Selected to_do']}
    #- for "Edit" it printed -> Event =  Edit , Value =  {'to_do': 'edited_todo', 'todos': ['Selected to_do']}
    #- for sg.WINDOW_CLOSED it printed -> Event =  None , Value =  {'to_do': None, 'todos': None}
    match event:
        case "Add":
            todos_from_file.append(value["to_do"] + "\n")
            fns.write_todos(todos_from_file)
            #- Update the window - specifically listbox(which has a key value of "to_do")
            #- with added to_do and before that strip the new lines before showing
            window["todos"].update(values=[todo.strip("\n") for todo in todos_from_file])
        case "Edit":
            selected_todo = value["todos"][0]       # [0] to get the string from the list 'todos': ['selected to_do']
            edited_todo = value["to_do"]
            #- Find the index of selected to-do
            index_of_selected_todo = todos_from_file.index(selected_todo + "\n")    # Selected to-do is stripped with "\n"
            #- Replace the selected to-do with edited to-do
            todos_from_file[index_of_selected_todo] = edited_todo + "\n"
            #- Write the new todos
            fns.write_todos(todos_from_file)
            #- Update the list box with edited to_do with stripped new lines
            window["todos"].update(values=[todo.strip("\n") for todo in todos_from_file])
        case "todos":
            #- Update the input (which has a key value of "to_do")
            window["to_do"].update(value=value['todos'][0])

        case sg.WINDOW_CLOSED:
            break

window.close()
