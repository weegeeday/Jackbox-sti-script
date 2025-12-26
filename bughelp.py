import FreeSimpleGUI as sg
Tab1 = [[sg.Text("Hello World! 1")]]
Tab2 = [[sg.Text("Hello World! 2")]]
Tab3 = [[sg.Text("Hello World! 3")]]
Tab4 = [[sg.Text("Hello World! 4")]]

Tabs = [[sg.Tab("1", Tab1),sg.Tab("2", Tab2), sg.Tab("3", Tab3), sg.Tab("4", Tab4)]]
TabGroup = [[sg.TabGroup(Tabs), sg.Button("test")]]
OtherFrame = [[sg.Text("Hello world!")]] #needs multiple frames, as its how its setup. ive got buttons that switch frames on and off.
button = [[sg.Button("switch 1",key="_s1_")],[sg.Button("switch 2",key="_s2_")]]

frames =  [[sg.Frame("", TabGroup,relief=sg.RELIEF_FLAT,expand_x=True,expand_y=True,grab=False,border_width=0,key="_F1_",element_justification="c",vertical_alignment="c",visible=True),
           sg.Frame("", OtherFrame,relief=sg.RELIEF_FLAT,expand_x=True,expand_y=True,grab=False,border_width=0,key="_F2_",element_justification="c",vertical_alignment="c",visible=False)]]

layout = [[sg.Column(button, element_justification='c'), sg.VSeperator(),sg.Column(frames, element_justification='c',key='_FC_')]]

window = sg.Window('STI Image Script', layout, size=(250,100))
while True:
    event, values = window.read(timeout=50)
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    if event == '_s1_':
        print("switch frames 1")
        window['_F1_'].update(visible=False)
        window['_F2_'].update(visible=True)
    if event == '_s2_':
        print("switch frames 2")
        window['_F1_'].update(visible=True)
        window['_F2_'].update(visible=False)
window.close()
