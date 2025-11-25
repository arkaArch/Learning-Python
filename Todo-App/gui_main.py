import modules.functions as fns
import FreeSimpleGUI as sg

layout = [[sg.Text("Type in a todo: ")],
          [sg.Input(key="to_do"), sg.Button("Add")]]

window = sg.Window("Todo app",
                   layout,
                   font=("Comfortaa-Light", 12))

while True:
    event, value = window.read()
    # print("Event = ", event, ", Value = ", value)
    #- Event =  Add , Value =  {'to_do': 'what I write in input box'}
    match event:
        case "Add":
            todos = fns.get_todos_from_file()
            todos.append(value["to_do"] + "\n")
            fns.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break

window.close()
