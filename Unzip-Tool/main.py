import FreeSimpleGUI as sg
from archive import  make_archive

completion_msg = sg.Text(key="completion_msg", text_color="yellow")
layout = [[sg.Text("Select files to compress: "),
           sg.Input(key="show_file_paths"),
           sg.FilesBrowse("Choose", key="file_paths")],
          [sg.Text("Select destination folder: "),
           sg.Input(key="show_folder_path"),
           sg.FolderBrowse("Choose", key="folder_path")],
          [sg.Button("Compress"),
           completion_msg]]

window = sg.Window("File Zipper", layout, font=("FiraCode Nerd Font", 12))

while True:
    event, values = window.read()
    print("Event = ", event, "\n",
          "Values = ", values)
    # Event = Compress
    # Values = {'show_file_paths': 'absolute-file-path-of-a.txt;absolute-file-path-of-b.txt;...',
    #           'file_paths': 'absolute-file-path-a.txt;absolute-file-path-b.txt;...',
    #           'show_folder_path': 'absolute-folder-path',
    #           'folder_path: 'absolute-folder-path'}

    match event:
        case "Compress":
            make_archive(values["file_paths"].split(";"), values["folder_path"])
            window["completion_msg"].update(value="Compression completed!")
        case sg.WINDOW_CLOSED:
            break

window.close()
