from PIL import Image
from random import seed
from random import randint
import os
import json
import time
randnO = 0
ImgNbR = 0
randnR = 0
tumbnb = 0
imgst = False
dir = "./Replacement Images"
dir_name = "./Original Images (STIPphoto)"
dir_name2 = "./Replacement Images"
dir_name3 = "./Images to put in STIPphoto"
seed(34587345)

class Main():
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
        fO = open("./IMGFO.txt", "w")
        ImgFO = sorted( filter( lambda x: os.path.isfile(os.path.join(dir_name, x)),
                        os.listdir(dir_name) ) )
        for file_name in ImgFO:
            fO.write(file_name)
            fO.write("\n")              
        fO.close()
        MRun.ImgFilterR()

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
            value = randint(0, ImgNbR - 1)
            randnR = value
            print("Random NBR genereated:")
            print(randnR)
            MRun.ImgIMCREX()

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
        im = Image.open("./Original Images (STIPphoto)/" + OImgO)
        imR = Image.open("./Replacement Images/" + OImgRO)
        im.close()
        imR = imR.resize((425, 320))
        imR = imR.convert("RGB")
        if not os.path.exists("./Images to put in STIPphoto/" + OImgO):
            imgst = True
            print("New image saved!")
            imR.save("./Images to put in STIPphoto/" + OImgO)
            os.remove("./Replacement Images/" + OImgRO) #might wanna replace this with copy but, fuck it.
            print("Replacement IMG used deleted!") #here copy command: os.popen('copy file1.txt file6.txt')
            MRun.tumb()
        print("IMG already exists...")
        imR.close()
        MRun.reset()
    
    @staticmethod
    def tumb():
        print("tumbnail method called")
        OImgO.rstrip(".jpg")
        ImgtO = OImgO + "-thumb.jpg"   
        imt = Image.open("./Images to put in STIPphoto/" + OImgO)
        imt = imt.resize((120, 90))
        imt = imt.convert("RGB")
        imt.save("./Images to put in STIPphoto/Thumbnails/" + ImgtO)
        print("Tumbnail saved!")
        imt.close()
        MRun.reset()

            
    
    @staticmethod
    def reset():
        print("Looping")
        time.sleep(1)
        MRun.genintO()
        

print("Make sure you have setup the image folders.")
print("WARNING: After an image is used to replace one in STIPphoto, it is DELETED.")
print("EXIT NOW if you havent made a backup of these images.")
print("waiting for 5 seconds...")
time.sleep(5)
MRun = Main()
MRun.genintO()        