import Data
import PySimpleGUI as sg

sg.theme('Dark Brown 1')
information = Data.information 


# Returning info depending on button increment/decrement
def get_info(index):
    keys = list(information.keys())
    if index < len(keys):
        key = keys[index]
        try:
            return int(information[key])
        except Exception:
            return information[key]
    else:
        return None


# GUI layout
layout = [
    [sg.Text("Index (Part name)"), sg.Input(key='-INPUT-')],
    [sg.Text("Results (Part info):", size=(0, 10), key='-PART-'), sg.Text("", key='-RESULT-', size=(50, 10),)],
    [sg.Button("Get Info"), sg.Button("Exit")]
]

# Create the window
window = sg.Window("Group 3 ACEBIO", layout, size=(700, 400))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Get Info":
        try:
            index = int(values['-INPUT-'])
            result = get_info(index)
            window['-RESULT-'].update(result)
        except ValueError as e:
            sg.popup_error(f"Enter a valid index. \n Error: {e}")



window.close()