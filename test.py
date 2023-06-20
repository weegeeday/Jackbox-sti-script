import PySimpleGUI as sg

data = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']

layout = [
    [sg.Listbox(values=data, size=(20, 5), key='-LISTBOX-', enable_events=True)],
    [sg.Button('Get Selected Index')]
]

window = sg.Window('Listbox Example', layout)

last_clicked_element = None

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-LISTBOX-':
        last_clicked_element = '-LISTBOX-'
    elif event == 'Get Selected Index':
        if last_clicked_element == '-LISTBOX-' and values['-LISTBOX-']:
            selected_indices = window['-LISTBOX-'].GetIndexes()
            if selected_indices:
                selected_index = selected_indices[0]
                print(selected_index)
                print(int(selected_index))
                sg.popup(f'Selected Index: {selected_index}')

window.close()
