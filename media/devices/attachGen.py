# Generates attachments for ribbons.
# Script runs independent of any parent directories.

from PIL import Image, ImageDraw

# Order or progression for knot devices
knots = [
    "1B",
    "2B",
    "3B",
    "4B",
    "1S",
    "2S",
    "3S",
    "4S",
    "1G",
    "2G",
    "3G",
    "4G"
]

# Order of progression for oak leaf cluster devices
leafs = [
    # "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20"
]

# Order of progression for valor w/ oak leaf cluster devices
valLeafs = [
    # "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20"
]

# Order of progression for numeral devices
numerals = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6"
]

# Order of progression for star devices
stars = [
    # "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10"
]



deviceTypes = {
    "knots": knots,
    "leafs": leafs,
    "valLeafs": valLeafs,
    "numberals": numerals,
    "stars": stars
}

selection = "knots"

ribbonName = "DSC"
background = Image.open("DSC.jpg")
foreground = Image.open("./media/leafs/13.png")

background.paste(foreground, (0,0), foreground)

background.save("test.png")

# for ribbon in deviceTypes[selection]:
#     image = Image.open("DSC.jpg")
#     draw = ImageDraw.Draw(image)

#     device = Image.open("./media/leafs/13.png")
    
#     x, y = device.size
#     draw.


    # out = Image.open("DSC.jpg") #Image.new("RGB", (100, 27))
    # out.paste(orgRibbon, (0, 0))
    # device = Image.open("./media/"+selection+"/"+ribbon+".png")
    # out.paste(device, (0,0))
    # out.save(ribbonName+"-"+ribbon+".png")
