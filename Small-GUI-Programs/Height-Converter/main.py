import FreeSimpleGUI as sg
from convert import feet_inches_to_cm

show_result = sg.Text(key="value_in_cm")
layout = [[sg.Text("Enter feet"), sg.Input(key="feet")],
          [sg.Text("Enter inches"), sg.Input(key="inches")],
          [sg.Button("Convert"), show_result]]

window = sg.Window("Height Convertor", layout, font=("FiraCode Nerd Font", 12))

while True:
    event, values = window.read()
    print(f" Event = {event}\n Values = {values}")
    # Event = Convert
    # Values = {'feet': '5', 'inches': '8'}

    match event:
        case "Convert":
            height_in_cm = feet_inches_to_cm(values["feet"], values["inches"])
            window["value_in_cm"].update(value=f"{height_in_cm} cm")
        case sg.WINDOW_CLOSED:
            break

window.close()
