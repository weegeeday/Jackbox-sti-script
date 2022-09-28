import PySimpleGUI as sg
import os
import Replacer
S = 0
sg.theme('dark grey 9')
dir = "./Replacement Images"
ImgR = next(os.walk(dir))[2]
imgC = len(ImgR)
layout = [  [sg.Text('Number of images to insert:' + str(imgC))],
            [sg.Text('Seed for randomness:'), sg.InputText('' + str(S)), sg.Button('Use Default')],
            [sg.Button('Run!'), sg.Button('Quit')] ]


window = sg.Window('STI Image Script', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit': # if user closes window or clicks cancel
        break
    if event == 'Run!' and int(values[0]) > 0 and int(values[0]) != None:
        print("helo fucker")
        Replacer.Replacer.reset()        
    else:
        sg.popup('Seed cannot be 0 or empty!')       
        
    if event == 'Use Default':
        Replacer.SeeD = 34587345
        S = 34587345
        window.refresh()
        
window.close()