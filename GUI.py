import PySimpleGUI as sg
import os
import Replacer
import winreg
S = 0
sg.theme('dark grey 9')
dir = "./Replacement Images"
ImgR = next(os.walk(dir))[2]
imgC = len(ImgR)
layout = [  [sg.Text('Number of images to insert:' + str(imgC))],
            [sg.Text('Seed for randomness:'), sg.InputText('',key='_h_'), sg.Button('Use Default')],
            [sg.Button('Run!'), sg.Button('Quit')] ]


window = sg.Window('STI Image Script', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit': # if user closes window or clicks cancel
        break
    if event == 'Run!' and values['_h_'] > str(0) and values['_h_'] != str(0):
        print("helo")
        Replacer.SeeD = int(values['_h_'])
        Replacer.dir_name = ""
        Replacer.Replacer.reset()                                             
    elif event == 'Run!':
        sg.popup('Seed cannot be 0 or empty!')
    if event == 'Use Default':
        Replacer.SeeD = 34587345
        values[0] = str(34587345)
        print(values[0])
        window['_h_'].update(values[0])
window.close()
