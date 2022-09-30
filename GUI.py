import PySimpleGUI as sg
import os
import Replacer
import winreg
S = 0
x = 0
winreg.HKEY_LOCAL_MACHINE
gif103 = sg.DEFAULT_BASE64_LOADING_GIF
SteamReg = ""
SteamINSD = ""
SteamST = ""
SteamINS = ""
sg.theme('dark grey 9')
dir = "./Replacement Images"
ImgR = next(os.walk(dir))[2]
imgC = len(ImgR)
layout = [  [sg.Text('Number of images to insert:' + str(imgC))],
            [sg.Text('Seed for randomness:'), sg.InputText('',key='_h_'), sg.Button('Use Default')], #move seed settings to settings tab and auto-set seed to default.
            [sg.Button('Run!'), sg.Button('Quit')] ]
layoutS = [  [sg.Text('Please wait attempting to get STI directory.')],
             [sg.Image(data=gif103, key='_IMAGE_', pad=(100,0))], #move seed settings to settings tab and auto-set seed to default.
             [sg.Button('Quit'), sg.ProgressBar(10,'horizontal',s=(10,10),bar_color=("blue","white"),expand_x=True,key='progressbar')] ]            


window = sg.Window('STI Image Script', layoutS)
progress_bar = window['progressbar']
event, values = window.read(timeout=50)
try:
    SteamReg = winreg.OpenKey(key=winreg.HKEY_LOCAL_MACHINE,sub_key="SOFTWARE\Valve\Steam",reserved=0,access=winreg.KEY_READ)
    progress_bar.Update(x+0.5)
    SteamINSD = winreg.QueryValueEx(SteamReg, "InstallPath")
    progress_bar.Update(x+0.5)
    SteamST = str(SteamINSD)
    SteamST = SteamST.removeprefix("('")
    SteamST = SteamST.removesuffix("', 1)")
    progress_bar.Update(x+1)
    SteamINS = SteamST
except FileNotFoundError:
    SteamReg = winreg.OpenKey(key=winreg.HKEY_LOCAL_MACHINE,sub_key="SOFTWARE\Wow6432Node\Valve\Steam",reserved=0,access=winreg.KEY_READ)
    progress_bar.Update(x+0.5)
    SteamINSD = winreg.QueryValueEx(SteamReg, "InstallPath")
    progress_bar.Update(x+0.5)
    SteamST = str(SteamINSD)
    SteamST = SteamST.removeprefix("('")
    SteamST = SteamST.removesuffix("', 1)")
    progress_bar.Update(x+1)
    SteamINS = SteamST
    #install directory gotten, just need to go into the steamapps folder and get libraryfolders.??? and parse it as json, get the id and in what path it is, then path trought
    #those files for the image folder.
while True:
    event, values = window.read(timeout=50)
    if event == sg.WIN_CLOSED or event == 'Quit': # if user closes window or clicks cancel
        break
    window.Element('_IMAGE_').UpdateAnimation(gif103,  time_between_frames=50)
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
