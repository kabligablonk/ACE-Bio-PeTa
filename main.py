import Data
import raspberry as rasp
import PySimpleGUI as sg

sg.theme('Dark Brown 1')
information = Data.information 

# Returning info depending on button increment/decrement
def get_info(index):
    keys = list(information.keys()) # Turn key names into natural language numbers
    if index < len(keys):
        key = keys[index]
        try:
            return int(information[key])
        except Exception:
            return information[key]
    else:
        return "Index out of range"

# GUI layout
layout = [
    [sg.Text("Index (Part name)"), sg.Input(key='-INPUT-')],
    [sg.Text("Results (Part info):", size=(0, 10), key='-PART-'), sg.Text("", key='-RESULT-', size=(50, 10),)],
    [sg.Button("Get Info"), sg.Button("Exit")]
]

# GUI for tracker window
tracker_window = [
    [sg.Text("Information Tracker")],
    [sg.Text("Index: "), sg.Text(rasp.dictionary_index, key='-INDEX-')]
]

# Create the window
window = sg.Window("Group 3 ACEBIO", layout, size=(700, 400))
tracker_window = sg.Window("Information Tracker", tracker_window, size=(200,400))

while True:
    event, values = window.read(timeout=100)  # Add timeout to periodically check for updates
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Get Info" or rasp.submit_pressed:
        try:
            index = int(values['-INPUT-'])
            result = get_info(index)
            window['-RESULT-'].update(result)
            window['-INPUT-'].update("")  # Clear the input field after getting info
            rasp.submit_pressed = False  # Reset the submit button state to false
        except ValueError as e:
            sg.popup_error(f"Enter a valid index. \n Error: {e}")

    # Update the index number based on button pressed
    window['-INPUT-'].update(rasp.dictionary_index)

window.close()