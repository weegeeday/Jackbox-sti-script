# Jackbox-sti-script
This script automaticly mods the Survive The Internet images. <br />
It does not mod the tumbnails as of the last time i updated this readme. <br />

# How do i use this?
Simple! <br />
1.Make sure you have python is installed, and its on your [PATH](https://datatofish.com/add-python-to-windows-path/ "Adding Python to PATH"). <br />
2.Run Setup.bat OR in cmd, run this: pip install -r requirements.txt <br />
3.Put the images you want the program to randomly replace in Replacement Images. <br />
5.Double Click GUI.py<br />

# Crashed? and other stuff.
If it crashes, leave a [github issue](https://github.com/weegeeday/Jackbox-sti-script/issues/new/choose). <br />
If you have any requests, suggestions or features youd want, make a [github issue](https://github.com/weegeeday/Jackbox-sti-script/issues/new/choose) about it! <br />
The program will not be able to work out Steam Libraries if you have more than 15 of them. <br />

# Linux Users, please read.
The way i have done the automatic detection of the steam library only supports windows. <br />
Please Change Variable dir_name in Replacer.py to the STIPphoto folder where the game is, and uncomment MRun.reset() at the bottom of Replacer.py. <br />
After this you will be able to run Replacer.py. <br />

