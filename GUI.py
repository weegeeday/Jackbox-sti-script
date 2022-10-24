from json import JSONDecoder
import json
import time
import PySimpleGUI as sg
import os
from PIL import Image
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
    os.mkdir("./Replacement ImagesP")
    os.mkdir("./Original ImagesP")
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
arrow = sg.SYMBOL_RIGHT_ARROWHEAD
SteamReg = ""
SteamINSD = ""
SteamST = ""
SteamINS = ""
Library = ""
z = 0
global layout
global ISDIR
global x3
global Linux
global ToolFR
global ToolSR
global SelectedToolBU
global imagefile
RRIcon = "iVBORw0KGgoAAAANSUhEUgAAALMAAAAeCAMAAABQSN/xAAAAAXNSR0IB2cksfwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAQVQTFRFAAAAIdF8IdF8IdF8IdF8IdF8IdF8IdF8IdF8IdF8IdF8IdF8IdF8IdF8IdF8IdF8////////////////////////////////////////////////////////////////////IdF8IdF8////////////////////////////////GZ5dHrhtHrluHrdt////////////////////AAAAC0InF41TC0EmHrdtIdF8E3pIE3tJFHtIHKplFHpIHrhu////IdF8F5RXF5NXAAAAC0MnF41TC0InFolRGZtcHrluGZhaGZhaEF84AAAAHK5nFYNNE3FDHK9oHK5nGqJg////////vsxuNwAAAFd0Uk5TAClmzHoUXP+PUuDCcNaZoxA/DkAwIJC/r/83/sCAoLDvH+twX39QT2/wYN+rqqvQ3+DPnwFLqUysRxkZlv+Wq489vL0CJVUlLe7/7fN9C7WphLP++gEEFMFrdwAAAwlJREFUeJztlWlb00AQx1cQKyB1a7JpV7ObSJrCBmoO8BbFW+tt0e//UZzZpJA2WRoPHnh8+n/Rbmf2+M3s7JSQhRb6r3VpaRl1eeW8QRrpSusqWV1rFVo/b5xGugagrRNtnDdPE7UntGtLq2T1eut319POHx17w6rabNZw8UaBvGyc4XS73V7NEbksftruxrU3b1Vtrjhtq5LmF7IrLcvzTTk4nVmv5XbVUcfcNM+3C+ZNc8fQ4fOAENYPQ9yWMZYPyCDsa2baD7fwq0O3Q4tMvJO1Cj/s3GgzK+zTnJluhWF+B+DcypktEoV9NLHtkBmCOC7nJbKzO9S6s1PHDB+eFJLDIaIXC8+Hg6USMgZmlrgizTDnriN5VHinmIUSjorAkLkiznJm4QmROgT3cUScT+Z7UuB825ciTuqLpWBut1fI7j4a7t67/2CGea/T6aki5MDF84EoDYiNly6BWYKRApGFEUmcmkbTaxnHHCowpDAVvJPaQEek6HGAmJvIx/ygr54Z+9xm+yEOh4Q8ekyeHDx9NsOcuooPYEC3D7uZj/nJDxCAqutZEzpeXtvaOnlOk7Ui64AgRu2ADTTzIOx1IUwpTy4F04DbYPSmR7nRWn9eDIdk/8XLV6/fvB3OMOPV4mXH3sAKYD8hZpj1AfCrhhm+A3i/IhUoVjC7eW3EgYVXU57MyXzmkobv3o9GHz5++lzDTFKZE0Ul5ijBXIEhRoMnDczQPEiQTDbT9Ss1cwoXQAFOZFVmfXXpXOYvX0eog2/fa5gjzrB8WVJixhKmGRoSpmvZwGxxRlWI8YHBt+EdWJoZQ8VHzTgAsmlmkVj00FDPJY3Hmnk0HtcwY6IdnqhybZCBShS+QfD42AwNzJhoO+Zdjr3BUwmiIDMs5w4WwUD5iZpmJo5STn1tlPvb0ajQkSkqWvlzsCsDo6hVBFGaahctkbDa9Vg8VZn625mp6f+zHUKTTGtdpv52ZnKiZvOYdF2H1rpM/e3s9OPn3+5g6m8XWab+dpFl6m8XWfP720ILLfTP9QtdQXEF0cojawAAAABJRU5ErkJggg=="
SRIcon = "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"
SIcon = "iVBORw0KGgoAAAANSUhEUgAAALMAAAAeCAMAAABQSN/xAAAAAXNSR0IB2cksfwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAIdQTFRFAAAAHbVsHbVsHbVsHbVsHbVsHbVsHbVsHbVsHbVs////////////HbVs////////////////////////////////HbVs////////HbVs////////HbVs////////////////////////HbVsHbVs////////////////////////HbVs////XmilpwAAAC10Uk5TAGb/zDNcKdbrRxA/IHpgr7+PT0D/gB/A8MJwoJmwXzDPf2+the9Q0N/gkAqfi0rfYgAAAm1JREFUeJztl317siAUxpmr2dC5lGO4zKlrSvrs+3++5wBOa9nCrHV1Xd1/8CYHf+INKCF3XUcPltLDtTmG6BaZHzXz47U5zDSZPhHyZGtmW5ank2szHZNtzZ6fZ1YjVbbPODx13DOOpvVi9ejFLNZ7nc/nfvBrHwbhGSh3tJj1Mc8WJrEcIs45wI9m4M1VlV2A+a0P2bLeDEKXEMuMLn+07zJfQB2mvVrZXc0gNIEdp7L3ICXSv5A5jkPTDDBztZ9lkuZB098N8pS4DlW9P9pmY7WYa7TD4rN9AINQDmlXQUSUL72gxLjKQu0NTGKsFaXsWhZYfA2BYVSheg1k/oa2tYNX5sjojSygTdktBCM0VN7t8TODgqekjDayK2BXVxSSuarwsV1vKHOD2WzJE1VZmUUmOEWZz2Qx1nPOi0PMlXy6WnLGMiE0ktmp6/N0ZsJqoQ1BIs25lOi9zGq5loDmEFVzGZmj4p32jHtJZhT1IsB3C99iB5jDttxcVnPOInxT+VDsxY6f/6133G2kEhIEEUyLHmVuXom2CCnrCoqBG8eIfaMRk4zVpmtomJMDzBzUvArNTKShBrp6xP7Mtm5ZQ9m2i0xlod6+95g9VS6hZU6HMq/7z8G1QSjf+IETfEEkD40KcjxCfDndMfh57iLVPM/ZPjPO8Ffug9zdWfbhOEHW0htqxPeGJ9SqS9QuR2tZjuT2QONITWIots+UjpmihQWL0TqpGqEqf7tLn6Z9zFPDYMa2j8LtylGJSKaUsVM+VS/8/bwvtQRLqEcM8ef/KTzL80wfjOP0h/+DXsIFX45Hvsn/7ltkvusurf+e+jX6cSOldAAAAABJRU5ErkJggg=="
IIcon = RRIcon
ISDIR = False
GUID = True
SteamLibrary = []
sg.theme_input_background_color("#1e1e1e")
sg.theme_input_text_color("white")
sg.theme_background_color("#121212")
sg.theme_element_text_color("white")
sg.theme_button_color(("#000000","#BB86FC"))
sg.theme_element_background_color("#121212")
sg.theme_text_element_background_color("#121212")
dir = "./Replacement Images"
ImgR = next(os.walk(dir))[2]
imgC = len(ImgR)
ImgFR = sorted( filter( lambda x: os.path.isfile(os.path.join(dir, x)),
                        os.listdir(dir) ) )
ToolRR = [  [sg.Text('Number of images to insert:' + str(imgC),key='_y_',auto_size_text=True,pad=((0,293),(0,0)))],
            [sg.Text('Seed for randomness:',key='_Seed_'), sg.InputText(key='_h_',size=(38,1)), sg.Button('Default', mouseover_colors=("#c394fc","#BB86FC"),font='_ 9 bold',key='_D_')], #move seed settings to settings tab and auto-set seed to default.
            [sg.Button('Run!', mouseover_colors=("#c394fc","#BB86FC"),font='_ 9 bold',key='_R_'), sg.Button('Quit', mouseover_colors=("#c394fc","#BB86FC"),font='_ 9 bold',key='_Q1_')] ]
layoutLOAD = [  [sg.Text('Please wait attempting to get STI directory.')],
                [sg.Image(data=gif103, key='_IMAGE_', pad=(100,0))], #move seed settings to settings tab and auto-set seed to default.
                [sg.Button('Quit',key='_Q_', mouseover_colors=("#c394fc","#BB86FC"),font='_ 9 bold'), sg.ProgressBar(10,'horizontal',s=(10,10),bar_color=("blue","white"),expand_x=True,key='_progressbar_')] ]
ToolRRLinux = [  [sg.Text('Nb of img to insert:' + str(imgC),key='_yL_',auto_size_text=True,pad=((0,329),(0,0)))],
                 [sg.Text("STIPhoto dir:"), sg.InputText(key='_LD_',pad=((0,88),(0,0)),size=(40,1))],
                 [sg.Text('Seed:',key='_SeedLinux_'), sg.InputText(key='_hL_',size=(38,1)), sg.Button('Default', mouseover_colors=("#c394fc","#BB86FC"),font='_ 9 bold',key='_D1_')], #move seed settings to settings tab and auto-set seed to default.
                 [sg.Button('Run!', mouseover_colors=("#c394fc","#BB86FC"),font='_ 9 bold',key='_R1_'), sg.Button('Quit', mouseover_colors=("#c394fc","#BB86FC"),font='_ 9 bold',key='_Q2_'), sg.Button('GUILibSettings',visible=True,disabled=False, mouseover_colors=("#c394fc","#BB86FC"),font='_ 9 bold')] ]

ToolO = [ [sg.Text("hello")] ]

ToolI = [ [sg.Text("hello")] ]

ToolSelect = [ [sg.Canvas(background_color="#121212",size=(10,10),key='_c1_')],
               [sg.Button(key='_RR_',mouseover_colors=("#323232","#505050"),button_color="#121212",border_width=0,expand_y=True,s=(10,1),image_data=RRIcon)],
               [sg.Canvas(background_color="#121212",size=(10,10),key='_c2_')],
               [sg.Button(key='_SR_',mouseover_colors=("#323232","#505050"),button_color="#121212",border_width=0,expand_y=True,s=(10,1),image_data=SRIcon)],
               [sg.Canvas(background_color="#121212",size=(10,10),key='_c3_')],
               [sg.Button(key='_S_',mouseover_colors=("#323232","#505050"),button_color="#121212",border_width=0,expand_y=True,s=(10,1),image_data=SIcon)],
               [sg.Canvas(background_color="#121212",size=(10,10),key='_c4_')],
               [sg.Button(key='_I_',mouseover_colors=("#323232","#505050"),button_color="#121212",border_width=0,expand_y=True,s=(10,1),image_data=IIcon)],
                 ]
window2 = sg.Window('STI Image Script', layoutLOAD)
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
    ToolFR = ToolRRLinux
    dir_nameL = "./"
    ImgFO = sorted( filter( lambda x: os.path.isfile(os.path.join(dir_nameL, x)),
                        os.listdir(dir_nameL) )) 
    ToolSR = [  [sg.Text("STIPhoto dir:"), sg.InputText(key='_STIPSRDIR_'),sg.Button("Set dir!",key="_SRSD_")],
                [sg.Listbox(ImgFR,select_mode="LISTBOX_SELECT_MODE_SINGLE",key='_LIST1L_',background_color="#121212",sbar_background_color="#505050",sbar_trough_color="#636363",sbar_arrow_color="white",sbar_frame_color="#505050",expand_y=True,expand_x=True,enable_events=True),sg.VSeparator(),sg.Listbox(ImgFO,select_mode="LISTBOX_SELECT_MODE_SINGLE",key='_LIST2L_',background_color="#121212",sbar_background_color="#505050",sbar_trough_color="#636363",sbar_arrow_color="white",sbar_frame_color="#505050",expand_y=True,expand_x=True,enable_events=True)], #move seed settings to settings tab and auto-set seed to default.
                [sg.Image(key="_SRRILIPL_"),sg.Text(arrow,auto_size_text=True),sg.Image(key="_SROILIPL_")],
                [sg.Button("Replace!",mouseover_colors=("#c394fc","#BB86FC"),font='_ 9 bold',key='_SRRBL_')],
                [sg.Button("Reload files!",key="_SRRFL_",mouseover_colors=("#c394fc","#BB86FC"),font='_ 9 bold')],
                [sg.Button('Quit', mouseover_colors=("#c394fc","#BB86FC"),font='_ 9 bold',key='_Q3_')] ]
    ToolWindow = [[sg.Frame('',ToolFR,background_color="#121212",relief=sg.RELIEF_FLAT,expand_x=True,expand_y=True,grab=False,border_width=0,key="_FRF_",element_justification="c",vertical_alignment="c",visible=True),
                   sg.Frame('',ToolSR,background_color="#121212",relief=sg.RELIEF_FLAT,expand_x=True,expand_y=True,grab=False,border_width=0,key="_SRF_",element_justification="c",vertical_alignment="c",visible=False, size=(500,200)),
                   sg.Frame('',ToolO,background_color="#121212",relief=sg.RELIEF_FLAT,expand_x=True,expand_y=True,grab=False,border_width=0,key="_OF_",element_justification="c",vertical_alignment="c",visible=False),
                   sg.Frame('',ToolI,background_color="#121212",relief=sg.RELIEF_FLAT,expand_x=True,expand_y=True,grab=False,border_width=0,key="_IF_",element_justification="c",vertical_alignment="c",visible=False)]]
    layout = [[sg.Column(ToolSelect, element_justification='c'), sg.VSeperator(),sg.Column(ToolWindow, element_justification='c',key='_ToolVC_')]]
    window = sg.Window('STI Image Script Linux/MacOSX', layout,size=(725,250))
    window.refresh()
elif Linux == False:
    ToolFR = ToolRR
    ImgFO = sorted( filter( lambda x: os.path.isfile(os.path.join(dir_name, x)),
                        os.listdir(dir_name) ) )
    ToolSR = [  [sg.Listbox(ImgFR,select_mode="LISTBOX_SELECT_MODE_SINGLE",key='_LIST1_',background_color="#121212",sbar_background_color="#505050",sbar_trough_color="#636363",sbar_arrow_color="white",sbar_frame_color="#505050",expand_y=True,expand_x=True,enable_events=True),sg.VSeparator(),sg.Listbox(ImgFO,select_mode="LISTBOX_SELECT_MODE_SINGLE",key='_LIST2_',background_color="#121212",sbar_background_color="#505050",sbar_trough_color="#636363",sbar_arrow_color="white",sbar_frame_color="#505050",expand_y=True,expand_x=True,enable_events=True)], #move seed settings to settings tab and auto-set seed to default.
                [sg.Image(key="_SRRILIP_"),sg.Text(arrow,auto_size_text=True),sg.Image(key="_SROILIP_")],
                [sg.Button("Replace!",mouseover_colors=("#c394fc","#BB86FC"),font='_ 9 bold',key='_SRRB_'),sg.Button("Reload files!",key="_SRRF_",mouseover_colors=("#c394fc","#BB86FC"),font='_ 9 bold'),sg.Button('Quit', mouseover_colors=("#c394fc","#BB86FC"),font='_ 9 bold',key='_Q3_')] ]
    ToolWindow = [[sg.Frame('',ToolFR,background_color="#121212",relief=sg.RELIEF_FLAT,expand_x=True,expand_y=True,grab=False,border_width=0,key="_FRF_",element_justification="c",vertical_alignment="c",visible=True),
                   sg.Frame('',ToolSR,background_color="#121212",relief=sg.RELIEF_FLAT,expand_x=True,expand_y=True,grab=False,border_width=0,key="_SRF_",element_justification="c",vertical_alignment="c",visible=False, size=(500,200)),
                   sg.Frame('',ToolO,background_color="#121212",relief=sg.RELIEF_FLAT,expand_x=True,expand_y=True,grab=False,border_width=0,key="_OF_",element_justification="c",vertical_alignment="c",visible=False),
                   sg.Frame('',ToolI,background_color="#121212",relief=sg.RELIEF_FLAT,expand_x=True,expand_y=True,grab=False,border_width=0,key="_IF_",element_justification="c",vertical_alignment="c",visible=False)]]
    layout = [[sg.Column(ToolSelect, element_justification='c'), sg.VSeperator(),sg.Column(ToolWindow, element_justification='c',key='_ToolVC_')]]
    window = sg.Window('STI Image Script Windows', layout,size=(725,250))
    window.refresh()
while True:
    event, values = window.read(timeout=50)
    ImgR = next(os.walk(dir))[2]
    imgC = len(ImgR)
    if Linux == True:
        window['_yL_'].update('Nb of img to insert:' + str(imgC))
        window.refresh()
    elif Linux == False:
        window['_y_'].update('Number of images to insert:' + str(imgC))
        window.refresh()
    if event == sg.WIN_CLOSED or event == '_Q_' or event == '_Q1_' or event == '_Q2_' or event == '_Q3_' : # if user closes window or clicks cancel
        break
    if event == '_R_' or event == '_R1_' and values['_h_'] > str(0) and values['_h_'] != str(0):
        print("helo")
        if Linux == True:
            if values['_LD_'] != "":
                fO4 = open("./Seed.txt", "w")
                fO4.write(str(values['_hL_']))
                fO4.close()
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
                window['_y2_'].update('Number of images to insert:' + str(imgC))
                time.sleep(0.5)
                sg.popup("Done!")        
            elif values['_LD_'] == "":
                sg.popup("STIPhoto directory cannot be empty!")               
        elif Linux == False:
            fO4 = open("./Seed.txt", "w")
            fO4.write(str(values['_h_']))
            fO4.close()
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
            time.sleep(0.5)
            sg.popup("Done!")                                             
    elif event == '_R_' or event == '_R1_':
        sg.popup('Seed cannot be 0 or empty!')
    if event == '_D_' or event == '_D1_':
        Replacer.SeeD = 34587345
        values[0] = str(34587345)
        print(values[0])
        window['_h_'].update(values[0])
    if event == 'GUILibSettings':
        sg.main_global_pysimplegui_settings()
    if event == '_RR_':
        print("selected tool FR")
        window['_RR_'].update(button_color="#323232")
        window['_SR_'].update(button_color="#121212")
        window['_S_'].update(button_color="#121212")
        window['_I_'].update(button_color="#121212")
        window['_IF_'].update(visible=False)
        window['_OF_'].update(visible=False)
        window['_FRF_'].update(visible=True)
        window['_SRF_'].update(visible=False)
    if event == '_SR_':
        print("selected tool SR")
        window['_SR_'].update(button_color="#323232")
        window['_RR_'].update(button_color="#121212")
        window['_S_'].update(button_color="#121212")
        window['_I_'].update(button_color="#121212")
        window['_IF_'].update(visible=False)
        window['_OF_'].update(visible=False)
        window['_FRF_'].update(visible=False)
        window['_SRF_'].update(visible=True)
    if event == '_S_':
        print("selected tool O")
        window['_S_'].update(button_color="#323232")
        window['_SR_'].update(button_color="#121212")
        window['_RR_'].update(button_color="#121212")
        window['_I_'].update(button_color="#121212")
        window['_IF_'].update(visible=False)
        window['_OF_'].update(visible=True)
        window['_FRF_'].update(visible=False)
        window['_SRF_'].update(visible=False)
    if event == '_I_':
        print("selected tool I")
        window['_I_'].update(button_color="#121212")
        window['_SR_'].update(button_color="#121212")
        window['_S_'].update(button_color="#121212")
        window['_RR_'].update(button_color="#121212")
        window['_IF_'].update(visible=True)
        window['_OF_'].update(visible=False)
        window['_FRF_'].update(visible=False)
        window['_SRF_'].update(visible=False)
    if Linux == True and event == '_SRSD_':
        dir_nameL = str(values['_STIPSRDIR_'])
        ImgFO = sorted( filter( lambda x: os.path.isfile(os.path.join(dir_nameL, x)),
                        os.listdir(dir_nameL) ))
        window['_LIST2L_'].update(ImgFO)
    if event == '_SRRF_':
        ImgFR = sorted( filter( lambda x: os.path.isfile(os.path.join(dir, x)),
                        os.listdir(dir) ) )
        ImgFO = sorted( filter( lambda x: os.path.isfile(os.path.join(dir_name, x)),
                        os.listdir(dir_name) ) )
        window['_LIST1_'].update(ImgFR)
    if event == '_SRRFL_':
        ImgFR = sorted( filter( lambda x: os.path.isfile(os.path.join(dir, x)),
                        os.listdir(dir) ) )
        ImgFO = sorted( filter( lambda x: os.path.isfile(os.path.join(dir_nameL, x)),
                        os.listdir(dir_nameL) ) )
        window['_LIST1L_'].update(ImgFR)
    if event == '_LIST1_':
        try:
            imagefile = dir + "/" + str(values['_LIST1_'][0])
            print(imagefile)
            img = Image.open(imagefile)
            head, sep, tail = str(values['_LIST1_'][0]).partition('.')
            print(head)
            img = img.resize((100,50))
            img.save("./Replacement ImagesP/" + head + ".png")
            imagef = "./Replacement ImagesP/" + head + ".png"
            window['_SRRILIP_'].update(source=imagef)
        except IndexError:
            sg.popup("No files in Replacement Images! Can't select anything!")
    if event == '_LIST1L_':
        try:
            imagefile = dir + "/" + str(values['_LIST1L_'][0])
            print(imagefile)
            img = Image.open(imagefile)
            head, sep, tail = str(values['_LIST1_'][0]).partition('.')
            print(head)
            img = img.resize((100,50))
            img.save("./Replacement ImagesP/" + head + ".png")
            imagef = "./Replacement ImagesP/" + head + ".png"
            window['_SRRILIPL_'].update(source=imagef)
        except IndexError:
            sg.popup("No files in Replacement Images! Can't select anything!")
    if event == '_LIST2_':
        try:
            imagefile = dir_name + "/" + str(values['_LIST2_'][0])
            print(imagefile)
            img = Image.open(imagefile)
            head, sep, tail = str(values['_LIST2_'][0]).partition('.')
            print(head)
            img = img.resize((100,50))
            img.save("./Original ImagesP/" + head + ".png")
            imagef = "./Original ImagesP/" + head + ".png"
            window['_SROILIP_'].update(source=imagef)
        except IndexError:
            sg.popup("No files in Replacement Images! Can't select anything!")
    if event == '_LIST2L_':      
        try:
            imagefile = dir_nameL + "/" + str(values['_LIST2L_'][0])
            print(imagefile)
            img = Image.open(imagefile)
            head, sep, tail = str(values['_LIST2L_'][0]).partition('.')
            print(head)
            img = img.resize((100,50))
            img.save("./Original ImagesP/" + head + ".png")
            imagef = "./Original ImagesP/" + head + ".png"
            window['_SROILIPL_'].update(source=imagef)
        except IndexError:
            sg.popup("No files in Replacement Images! Can't select anything!")
    if event == '_SRRB_':
        fO5 = open("./dir_name.txt", "w")
        fO5.write(str(dir_name))
        fO5.close()
        Orimg = str(values['_LIST2_'][0])
        Reimg = str(values['_LIST1_'][0])
        Replacer.Replacer.SRTOOL(Reimg,Orimg)
        ImgFR = sorted( filter( lambda x: os.path.isfile(os.path.join(dir, x)),
                        os.listdir(dir) ) )
        window['_LIST1_'].update(ImgFR)
        sg.popup("Done!")
    if event == '_SRRBL_':
        fO5 = open("./dir_name.txt", "w")
        fO5.write(str(values['_LD_']))
        fO5.close()
        Orimg = str(values['_LIST2L_'][0])
        Reimg = str(values['_LIST1L_'][0])
        Replacer.Replacer.SRTOOL(Reimg,Orimg)
        ImgFR = sorted( filter( lambda x: os.path.isfile(os.path.join(dir, x)),
                        os.listdir(dir) ) )
        window['_LIST1L_'].update(ImgFR)
        sg.popup("Done!")
window.close()