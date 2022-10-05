import os
from PIL import Image
from PIL import ImageOps
im = Image.open("./test.jpg")
exif = im.getexif()
im.close()
yp = open("./testexif.txt", "w")
yp.write(str(exif))
yp.close()
im2 = Image.open("./Statue.jpg")
exif2 = im2.getexif()
yp2 = open("./statueexif.txt", "w")
yp2.write(str(exif2))
yp2.close()
im2.close()
im3 = Image.open("./Statue-thumb.jpg")
exif3 = im3.getexif()
yp3 = open("./statuetumbexif.txt", "w")
yp3.write(str(exif3))
im3.close()


im = Image.open("./test.jpg")
im = im.resize((425, 320))
im = im.convert("RGB")