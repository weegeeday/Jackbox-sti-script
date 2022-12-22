import os
import random
import time
from PIL import Image

import PySimpleGUI as sg


class Replacer:
    def __init__(self, seeD):
        self.dir_name = "./Replacement Images"
        self.dir_name2 = ".\Replacement Images"
        self.dir_name3 = ".\Images to put in STIPphoto"
        self.image_number = 0
        self.replacement_number = 0
        self.original_image = ""
        self.replacement_image = ""
        self.imgst = False
        self.seed = seeD

    def genintO(self):
        self.image_number = random.randint(0, 131)
        print("Random NBO generated:")
        print(self.image_number)
        self.img_count_r()

    def img_count_r(self):
        images = next(os.walk(self.dir_name))[2]
        print("Number of Replacement Images Counted:")
        self.replacement_count = len(images)
        print(self.replacement_count)
        self.img_filter_o()

    def img_filter_o(self):
        with open("./dir_name.txt", "r") as f:
            self.dir_name = f.read()
        print(self.dir_name)
        try:
            image_files = sorted(
                filter(
                    lambda x: os.path.isfile(os.path.join(self.dir_name, x)),
                    os.listdir(self.dir_name),
                )
            )
            with open("./IMGFO.txt", "w") as f:
                for file_name in image_files:
                    f.write(file_name)
                    f.write("\n")
            self.img_filter_r()
        except FileNotFoundError:
            print("invalid dir.")
            sg.popup("Invalid directory was set!")
            self.crash()

    def img_filter_r(self):
        with open("./IMGFR.txt", "w") as f:
            image_files = sorted(
                filter(
                    lambda x: os.path.isfile(os.path.join(self.dir_name2, x)),
                    os.listdir(self.dir_name2),
                )
            )
            for file_name in image_files:
                f.write(file_name)
                f.write("\n")
        self.genint_r()

    def genint_r(self):
        try:
            self.replacement_number = random.randint(0, self.replacement_count - 1)
            print("Random NBR generated:")
            print(self.replacement_number)
            self.img_im_crex()
        except ValueError:
            print("hello crash")
            self.crash()

    def img_im_crex(self):
        with open("./IMGFO.txt", "r") as f:
            original_images = f.readlines()
        with open("./IMGFR.txt", "r") as f:
            replacement_images = f.readlines()
        self.original_image = original_images[self.image_number].rstrip("\n")
        self.replacement_image = replacement_images[self.replacement_number].rstrip("\n")

        with Image.open(self.dir_name + "/" + self.original_image) as im:
            with Image.open("./Replacement Images/" + self.replacement_image) as im_r:
                im_r = im_r.resize((425, 320))
                im_r = im_r.convert("RGB")
                if not os.path.exists(
                    "./Images to put in STIPphoto/" + self.original_image
                ):
                    im_r.save(
                        "./Images to put in STIPphoto/" + self.original_image
                    )
                    self.imgst = True
                else:
                    self.imgst = False
                    sg.popup("An image with the same name already exists!")
                    self.crash()

    def crash(self):
        print("crash")
        time.sleep(3)
        exit()

    def tumb(self):
        print("tumbnail method called")
        original_image_name = self.original_image.rstrip(".jpg")
        thumbnail_name = original_image_name + "-thumb.jpg"
        with Image.open(
            "./Images to put in STIPphoto/" + self.original_image
        ) as imt:
            imt = imt.resize((120, 90))
            imt = imt.convert("RGB")
            imt.save("./Images to put in STIPphoto/Thumbnails/" + thumbnail_name)
            print("Tumbnail saved!")

    def reset(self):
        print(self.seed)
        images = next(os.walk(self.dir_name))[2]
        if len(images) == 0:
            print("replacement img count == 0, crashing.")
            self.crash()
        elif len(images) != 0:
            print("Looping")
            time.sleep(1)
            self.genintO()

    def SRTOOL(self, reimg, orimg):
        DIR = open("./dir_name.txt", "r")
        self.dir_name = DIR.read()
        with Image.open(str(self.dir_name + "/" + reimg)) as pre:
            pre = pre.resize((425, 320))
            pre = pre.convert("RGB")
            pre.save("./Images to put in STIPphoto/" + orimg)
            os.replace(
                "./Replacement Images/" + reimg,
                "./Replacement Images Backup/" + reimg,
            )
            pre = pre.resize((120, 90))
            orimg2 = orimg.rstrip(".jpg")
            orimgT = orimg2 + "-thumb.jpg"
            pre.save("./Images to put in STIPphoto/Thumbnails/" + orimgT)

def main():
    replacer = Replacer()
    replacer.reset()

if __name__ == "__main__":
    main()
