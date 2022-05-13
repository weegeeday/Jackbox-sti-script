from PIL import Image
from random import seed
from random import randint
import os
import json
randnO = 0
ImgNbR = 0
dir = "./Replacement Images"
dir_name = "./Original Images (STIPphoto)"
dir_name2 = "./Replacement Images"
seed(34587345)

class Main():
    @staticmethod
    def genintO():
        for _ in range(1):
            value = randint(0, 131)
            randnO = value
            print("Random NB genereated:")
            print(randnO)
            MRun.ImgCountR()

    @staticmethod
    def ImgCountR():
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
        MRun.ImgIMCREX()

    @staticmethod
    def ImgIMCREX():
        f = open("./IMGFO.txt", "r")
        o = open("./IMGFR.txt", "r")
        OImg = f.readlines()
        OImgR = o.readlines()
        OImgO = OImg[randnO].rstrip("\n")
        OImgRO = OImgR[randnO].rstrip("\n")
        im = Image.open("./Original Images (STIPphoto)/" + OImgO)
        imR = Image.open("./Replacement Images/" + OImgRO)
        (width, height) = (im.width // 2, im.height // 2)
        im.close()
        imR.resize((width, height))
        imR.convert("RGB")
        imR.save("./Images to put in STIPphoto/" + OImgO)
        MRun.reset()

    @staticmethod
    def reset():
        randnO = 0
        ImgNbR = 0
        MRun.genintO()

print("Make sure you have setup the image folders.")
MRun = Main()
MRun.genintO()        