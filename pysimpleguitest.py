import PySimpleGUI as sg
import pyperclip as pc
result = ''
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Welcome to tempature converter')],
            [sg.Text('What is the number you would like to convert'), sg.InputText()],
            [sg.Text('Enter "1" to convert celsius to fahrenheit. Enter "2" to convert fahrenheit to celcius'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Tempature Converter', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if values[1] == '1':
            result = ((((int(values[0])) * 9/5) + 32))
    elif values[1] == '2':
              result = ((((int(values[0])) - 32) * 5/9))
    else:
              result = 'Invalid Value'
    layout2 = [  [sg.Text(result)]]
    window = sg.Window('Result', layout2)
    pc.copy(result)

window.close()
