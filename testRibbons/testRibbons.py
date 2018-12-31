'''
Creates a defined number of test ribbon images.
Each image has the dimensions of 100x27 with a
white background. Each image will also have a
number centered on it to help easily distinguish
between each ribbon.

'''

from PIL import Image, ImageFont, ImageDraw

ribbonNum = 50 # Amount of ribbons to create

for x in range(1, ribbonNum+1):
    img = Image.new("RGB", (100, 27), color="White")
    draw = ImageDraw.Draw(img)

    textFont = ImageFont.truetype("arial.ttf", 25)

    if x < 10:
        xCoord = 45
    else:
        xCoord = 37

    draw.text((xCoord,0), str(x), (0,0,0), font=textFont)
    img.save(str(x)+".png")