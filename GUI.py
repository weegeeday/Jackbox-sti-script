from json import JSONDecoder
import json
import time
from tkinter.tix import TEXT
import PySimpleGUI as sg
import os
PREP1 = open("./Library.json", "w")
PREP1.close()
PREP2 = open("./dir_name.txt", "w")
PREP2.close()
PREP3 = open("./Seed.txt", "w")
PREP3.close()
try: 
    os.mkdir("./Replacement Images")
    os.mkdir("./Replacement Images Backup")
    os.mkdir("./Images to put in STIPphoto")
    os.mkdir("./Images to put in STIPphoto/Thumbnails")
except FileExistsError:
    print("skipping making folders.")
import Replacer
import winreg
import vdf
S = 0
x = 0
y = 0
x2 = 6.5
winreg.HKEY_LOCAL_MACHINE
gif103 = sg.DEFAULT_BASE64_LOADING_GIF
SteamReg = ""
SteamINSD = ""
SteamST = ""
SteamINS = ""
Library = ""
z = 0
global ISDIR
global x3
global Linux
ISDIR = False
GUID = True
SteamLibrary = []
sg.theme('dark grey 9')
dir = "./Replacement Images"
ImgR = next(os.walk(dir))[2]
imgC = len(ImgR)
layout = [  [sg.Text('Number of images to insert:' + str(imgC),key='_y_'), sg.Checkbox("Dev",key='_DCH_',visible=False)],
            [sg.Text('Seed for randomness:'), sg.InputText('',key='_h_'), sg.Button('Use Default')], #move seed settings to settings tab and auto-set seed to default.
            [sg.Button('Run!'), sg.Button('Quit'), sg.Button('GUILibSettings',visible=False,disabled=False)] ]
layoutS = [  [sg.Text('Please wait attempting to get STI directory.')],
             [sg.Image(data=gif103, key='_IMAGE_', pad=(100,0))], #move seed settings to settings tab and auto-set seed to default.
             [sg.Button('Quit',key='_h2_'), sg.ProgressBar(10,'horizontal',s=(10,10),bar_color=("blue","white"),expand_x=True,key='_progressbar_')] ]
layoutLI = [  [sg.Text('Number of images to insert:' + str(imgC),key='_y_'), sg.Checkbox("Dev",key='_DCH_',visible=True)],
            [sg.Text("STIPhoto directory:"), sg.InputText('',key='_LD_')],
            [sg.Text('Seed for randomness:'), sg.InputText('',key='_h_'), sg.Button('Use Default')], #move seed settings to settings tab and auto-set seed to default.
            [sg.Button('Run!'), sg.Button('Quit'), sg.Button('GUILibSettings',visible=False,disabled=False)] ]            
window2 = sg.Window('STI Image Script', layoutS)
progress_bar = window2['_progressbar_']
event, values = window2.read(timeout=50)
try:
    SteamReg = winreg.OpenKey(key=winreg.HKEY_LOCAL_MACHINE,sub_key="SOFTWARE\Valve\Steam",reserved=0,access=winreg.KEY_READ)
    Linux = False
    progress_bar.Update(x+0.5) #0.5
    SteamINSD = winreg.QueryValueEx(SteamReg, "InstallPath")
    progress_bar.Update(x+1) #1
    SteamST = str(SteamINSD)
    SteamST = SteamST.removeprefix("('")
    SteamST = SteamST.removesuffix("', 1)")
    progress_bar.Update(x+2) #2
    SteamINS = SteamST
    #install directory gotten, just need to go into the steamapps folder and get libraryfolders.??? and parse it as json, get the id and in what path it is, then path trought
    #those files for the image folder.
    Library = SteamST + "\\steamapps\\libraryfolders.vdf"
    progress_bar.Update(x+2.5) #2.5
    LibraryP = vdf.parse(open(Library))
    progress_bar.Update(x+3) #3
    fO = open("./Library.json", "w")
    fO.write(str(LibraryP))
    fO.close()
    progress_bar.Update(x+3.5)#3.5
    fO2 = open("./Library.json", "r")
    filedata = fO2.read()
    fO2.close()
    filedata = filedata.replace('\'', '\"')
    progress_bar.Update(x+4)#4
    fO3 = open("./Library.json", "w")
    fO3.write(filedata)
    fO3.close()
    progress_bar.Update(x+5)
    FO = open("./Library.json", "r")
    LibraryJ1 = json.loads(FO.read())
    FO.close()
    progress_bar.Update(x+6.5)
    while True:
        event, values = window2.read(timeout=50)
        try:
            SteamLibrary.append(LibraryJ1['libraryfolders'][str(y)]['path'])
            y = int(y) + 1
            print("z" + str(z))
            print("y" + str(y))
            progress_bar.Update(x2)
            x2 = x2 + 0.25
        except KeyError:
            print("keyerror")
            if ISDIR == True:
                x3 = 10 - x2
                x4 = x2 + x3/2
                x5 = x4 + x3/2 
                break
            while ISDIR == False:
                print("testing dir")
                try:
                    print(z)
                    ISDIR = os.path.isdir(str(SteamLibrary[z]) + "\\steamapps\\common\\The Jackbox Party Pack 4\\games\\SurviveTheInternet\\content\\STIPhoto")
                    z = z + 1
                    print(z)
                    print(ISDIR)
                except IndexError:
                    print("indexerror")
                    z = z - 1
                    dir_name = str(SteamLibrary[z]) + "\\steamapps\\common\\The Jackbox Party Pack 4\\games\\SurviveTheInternet\\content\\STIPhoto"
                    print("break")
                    raise
except FileNotFoundError:
    try:
        SteamReg = winreg.OpenKey(key=winreg.HKEY_LOCAL_MACHINE,sub_key="SOFTWARE\Wow6432Node\Valve\Steam",reserved=0,access=winreg.KEY_READ)
        Linux = False
        progress_bar.Update(x+0.5) #0.5
        SteamINSD = winreg.QueryValueEx(SteamReg, "InstallPath")
        progress_bar.Update(x+1) #1
        SteamST = str(SteamINSD)
        SteamST = SteamST.removeprefix("('")
        SteamST = SteamST.removesuffix("', 1)")
        progress_bar.Update(x+2) #2
        SteamINS = SteamST
        #install directory gotten, just need to go into the steamapps folder and get libraryfolders.??? and parse it as json, get the id and in what path it is, then path trought
        #those files for the image folder.
        Library = SteamST + "\\steamapps\\libraryfolders.vdf"
        progress_bar.Update(x+2.5) #2.5
        LibraryP = vdf.parse(open(Library))
        progress_bar.Update(x+3) #3
        fO = open("./Library.json", "w")
        fO.write(str(LibraryP))
        fO.close()
        progress_bar.Update(x+3.5)#3.5
        fO2 = open("./Library.json", "r")
        filedata = fO2.read()
        fO2.close()
        filedata = filedata.replace('\'', '\"')
        progress_bar.Update(x+4)#4
        fO3 = open("./Library.json", "w")
        fO3.write(filedata)
        fO3.close()
        progress_bar.Update(x+5)
        FO = open("./Library.json", "r")
        LibraryJ1 = json.loads(FO.read())
        FO.close()
        progress_bar.Update(x+6.5)
        while True:
            event, values = window2.read(timeout=50)
            try:
                SteamLibrary.append(LibraryJ1['libraryfolders'][str(y)]['path'])
                y = int(y) + 1
                print("z" + str(z))
                print("y" + str(y))
                progress_bar.Update(x2)
                x2 = x2 + 0.25
            except KeyError:
                print("keyerror")
                if ISDIR == True:
                    x3 = 10 - x2
                    x4 = x2 + x3/2
                    x5 = x4 + x3/2
                    z = z - 1
                    dir_name = str(SteamLibrary[z]) + "\\steamapps\\common\\The Jackbox Party Pack 4\\games\\SurviveTheInternet\\content\\STIPhoto" 
                    break
                while ISDIR == False:
                    print("testing dir")
                    try:                                        
                        print(z)
                        ISDIR = os.path.isdir(str(SteamLibrary[z]) + "\\steamapps\\common\\The Jackbox Party Pack 4\\games\\SurviveTheInternet\\content\\STIPhoto")
                        z = z + 1
                        print(z)
                        print(ISDIR)
                    except IndexError:
                        print("indexerror")
                        z = z - 1
                        dir_name = str(SteamLibrary[z]) + "\\steamapps\\common\\The Jackbox Party Pack 4\\games\\SurviveTheInternet\\content\\STIPhoto"
                        print(dir_name)
                        print("break")
                        raise
    except FileNotFoundError:
        print("On linux. Tried to use GUI.")
        Linux = True
        sg.popup_error_with_traceback("STI Linux GUI Error","Hi! It seems as you are running the GUI script on Linux/MacOSX.","You will need to manually set STIPhoto directory.","ex: \\steamapps\\common\\The Jackbox Party Pack 4\\games\\SurviveTheInternet\\content\\STIPhoto","PySimpleGUI settings checkbox (click on dev box!) has been enabled.")
        x2 = x2 + 0.25
        x3 = 10 - x2
        x4 = x2 + x3/2
        x5 = x4 + x3/2
        z = z - 1

time.sleep(0.5)
progress_bar.Update(x4)
time.sleep(0.5)
progress_bar.Update(x5)
time.sleep(0.5)     
window2.close()       
if Linux == True:
    window = sg.Window('STI Image Script Linux/MacOSX', layoutLI)
elif Linux == False:
    window = sg.Window('STI Image Script Windows', layout)
while True:
    event, values = window.read(timeout=50)
    if Linux == True:
        window["_DCH_"].update(visible=True)
        window['GUILibSettings'].update(visible=True)
        window.refresh()
    elif Linux == False:
        window["_DCH_"].update(visible=False)
        window['GUILibSettings'].update(visible=False)
        window.refresh()
    if event == sg.WIN_CLOSED or event == 'Quit': # if user closes window or clicks cancel
        break
    if event == 'Run!' and values['_h_'] > str(0) and values['_h_'] != str(0):
        print("helo")
        fO4 = open("./Seed.txt", "w")
        fO4.write(str(values['_h_']))
        fO4.close()
        if Linux == True:
            if values['_LD_'] != "":
                fO5 = open("./dir_name.txt", "w")
                fO5.write(str(values['_LD_']))
                fO5.close()
                fO6 = open("./dir_name.txt", "r")
                filedata2 = fO6.read()
                fO6.close()
                time.sleep(0.5)
                print(filedata2)
                fO7 = open("./dir_name.txt", "w")
                fO7.write(filedata2)
                fO7.close()
                Replacer.Replacer.reset()
                ImgR = next(os.walk(dir))[2]
                imgC = len(ImgR)
                window['_y_'].update('Number of images to insert:' + str(imgC))
                time.sleep(0.5)
                sg.popup("Done!")        
            elif values['_LD_'] == "":
                sg.popup("STIPhoto directory cannot be empty!")               
        elif Linux == False:
            fO5 = open("./dir_name.txt", "w")
            fO5.write(str(dir_name))
            fO5.close()
            fO6 = open("./dir_name.txt", "r")
            filedata2 = fO6.read()
            fO6.close()
            time.sleep(0.5)
            print(filedata2)
            fO7 = open("./dir_name.txt", "w")
            fO7.write(filedata2)
            fO7.close()
            Replacer.Replacer.reset()
            ImgR = next(os.walk(dir))[2]
            imgC = len(ImgR)
            window['_y_'].update('Number of images to insert:' + str(imgC))
            time.sleep(0.5)
            sg.popup("Done!")                                             
    elif event == 'Run!':
        sg.popup('Seed cannot be 0 or empty!')
    if event == 'Use Default':
        Replacer.SeeD = 34587345
        values[0] = str(34587345)
        print(values[0])
        window['_h_'].update(values[0])
    if values['_DCH_'] == True:
       window['GUILibSettings'].update(visible=True)
       window.refresh()
    if values['_DCH_'] == False:
           window['GUILibSettings'].update(visible=False)
           window.refresh()
    if event == 'GUILibSettings':
        sg.main_global_pysimplegui_settings()
window.close()
