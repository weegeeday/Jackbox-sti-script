from PIL import Image
from random import seed
from random import randint
import os
import time
import PySimpleGUI as sg
randnO = 0
ImgNbR = 0
randnR = 0
tumbnb = 0
SeeD = 0
imgst = False
dir = "./Replacement Images"
dir_name2 = ".\Replacement Images"
dir_name3 = ".\Images to put in STIPphoto"
fO1 = open("./Seed.txt", "r")
fO1.readline(1)
seed(fO1.readline(1))
fO1.close()

class Replacer():
    @staticmethod
    def genintO():
        global randnO
        for _ in range(1):
            value = randint(0, 131)
            randnO = value
            print("Random NBO genereated:")
            print(randnO)
            MRun.ImgCountR()

    @staticmethod
    def ImgCountR():
        global ImgNbR
        ImgR = next(os.walk(dir))[2]
        print("Number of Replacement Images Counted:")
        ImgNbR = len(ImgR)
        print(ImgNbR)
        MRun.ImgFilterO()

    @staticmethod
    def ImgFilterO():
        global dir_name
        global DIR
        fO = open("./IMGFO.txt", "w")
        DIR = open("./dir_name.txt", "r")
        dir_name = DIR.read()
        print(dir_name)
        try:
            ImgFO = sorted( filter( lambda x: os.path.isfile(os.path.join(dir_name, x)),
                        os.listdir(dir_name) ) )
            for file_name in ImgFO:
                fO.write(file_name)
                fO.write("\n")              
            fO.close()
            DIR.close()
            MRun.ImgFilterR()
        except FileNotFoundError:
            print("invalid dir.")
            sg.popup("Invalid directory was set!")           
            MRun.crash()

    @staticmethod
    def ImgFilterR():
        fR = open("./IMGFR.txt", "w")
        ImgFR = sorted( filter( lambda x: os.path.isfile(os.path.join(dir_name2, x)),
                        os.listdir(dir_name2) ) )
        for file_name in ImgFR:
            fR.write(file_name)
            fR.write("\n")              
        fR.close()
        MRun.genintR()
    
    @staticmethod
    def genintR():
        global randnR
        for _ in range(1):
            try:
                value = randint(0, ImgNbR - 1)
                randnR = value
                print("Random NBR genereated:")
                print(randnR)
                MRun.ImgIMCREX()
            except ValueError:
                print("hello crash")
                MRun.crash()
#make new method for SRTool
    @staticmethod
    def ImgIMCREX():
        global OImgO
        global imgst
        f = open("./IMGFO.txt", "r")
        o = open("./IMGFR.txt", "r")
        OImg = f.readlines()
        OImgR = o.readlines()
        OImgO = OImg[randnO].rstrip("\n")
        OImgRO = OImgR[randnR].rstrip("\n")
        im = Image.open(dir_name +"/" + OImgO)
        imR = Image.open("./Replacement Images/" + OImgRO)
        im.close()
        imR = imR.resize((425, 320))
        imR = imR.convert("RGB")
        if not os.path.exists("./Images to put in STIPphoto/" + OImgO):
            imgst = True
            print("New image saved!")
            imR.save("./Images to put in STIPphoto/" + OImgO)
            os.replace("./Replacement Images/" + OImgRO, "./Replacement Images Backup/" + OImgRO)           
            print("Replacement IMG used moved!")
            MRun.tumb()
        print("IMG already exists...")
        imR.close()
        MRun.reset()
    
    @staticmethod
    def tumb():
        print("tumbnail method called")
        OImgO2 = OImgO.rstrip(".jpg")
        ImgtO = OImgO2 + "-thumb.jpg"   
        imt = Image.open("./Images to put in STIPphoto/" + OImgO)
        imt = imt.resize((120, 90))
        imt = imt.convert("RGB")
        imt.save("./Images to put in STIPphoto/Thumbnails/" + ImgtO)
        print("Tumbnail saved!")
        imt.close()
        MRun.reset()

            
    
    @staticmethod
    def reset():
        print(SeeD)
        ImgR = next(os.walk(dir))[2]
        if len(ImgR) == 0:
            print("replacement img count == 0, crashing.")
            MRun.crash()
        elif len(ImgR) != 0:
            print("Looping")
            time.sleep(1)
            MRun.genintO()
    
    @staticmethod
    def crash():
        try:
            print("crashing to return to GUI.py")
            fR = open("./crash.txt", "r")
            fR.readlines()
        except FileNotFoundError:
            print("hello fillenotfounderror")
    @staticmethod
    def SRTOOL(Reimg,Orimg):
        global imgst
        DIR = open("./dir_name.txt", "r")
        dir_name = DIR.read()
        Pre = Image.open(str(dir + "/" + Reimg))
        Dor = str(dir_name + "\\" + Orimg)
        Pre = Pre.resize((425, 320))
        Pre = Pre.convert("RGB")
        Pre.save("./Images to put in STIPphoto/" + Orimg)
        os.replace("./Replacement Images/" + Reimg, "./Replacement Images Backup/" + Reimg)
        Pre = Pre.resize((120, 90))
        Orimg2 = Orimg.rstrip(".jpg")
        OrimgT = Orimg2 + "-thumb.jpg"        
        Pre.save("./Images to put in STIPphoto/Thumbnails/" + OrimgT)          
MRun = Replacer()
#MRun = MRun.reset()