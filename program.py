from PIL import Image
import json

from library import ribbonBuilder, parseMilpac

def testRibbons():
    '''Function built for testing scalability of ribbon racks'''

    print("Enter amount of ribbons to generate:")
    num = int(input())

    grid = ribbonBuilder(num).setupGrid()
    imgRack = Image.new("RGBA", (ribbonBuilder(num).rackDimensions()["width"], ribbonBuilder(num).rackDimensions()["height"]))

    for val in range(0, num):
        ribbon = Image.open("./testRibbons/"+str(val+1)+".png")
        imgRack.paste(ribbon, (grid[val][0], grid[val][1]))
        
    imgRack.save("Ribbon Rack.png", "PNG")

    return 0


def rackImage():
    "Builds .png test file of a trooper's ribbon rack"

    print("Enter trooper's Milpac ID:")
    ID = input()
    indAwards = parseMilpac(int(ID)).indAwards()

    ribbons = []
    for val in indAwards:
        if val["count"] >= 1:
            ribbons.append(val)
    ribbons.reverse()

    ribbonCount = len(ribbons)

    grid = ribbonBuilder(ribbonCount).setupGrid()
    imgRack = Image.new("RGBA", (ribbonBuilder(ribbonCount).rackDimensions()["width"], ribbonBuilder(ribbonCount).rackDimensions()["height"]))

    for indx, val in enumerate(ribbons): # Build ribbons
        device = Image.open("./media/devices/"+str(val["device"])+"/"+str(val["count"])+".png")
        ribbon = Image.open("./media/ribbons/"+str(val["shortName"])+".png")
        ribbon.paste(device, (0,0), device)
        imgRack.paste(ribbon, (grid[indx][0], grid[indx][1]))

    imgRack.save("{}.png".format(ID), "PNG")

    return 0

if __name__ == "__main__":
    rackImage()
