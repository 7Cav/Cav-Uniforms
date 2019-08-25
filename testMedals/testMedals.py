'''
Creates a defined number of test ribbon images.
Each image has the dimensions of 100x27 with a
white background. Each image will also have a
number centered on it to help easily distinguish
between each ribbon.

Script functions independently of any parent directories.
'''

from PIL import Image, ImageFont, ImageDraw
import os

# Changes working directory so working path is current location.
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

ribbonWidth = 43
ribbonHeight = 13

ribbonNum = 50 # Amount of ribbons to create

for x in range(1, ribbonNum+1):
    img = Image.new("RGB", (ribbonWidth, ribbonHeight), color="White")
    draw = ImageDraw.Draw(img)

    textFont = ImageFont.truetype("arial.ttf", 14)

    if x < 10:
        xCoord = 18
    else:
        xCoord = 13

    draw.text((xCoord,-.5), str(x), (0,0,0), font=textFont)
    img.save(str(x)+".png")