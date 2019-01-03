import webbrowser  # NOTE FOR DEBUGGING ONLY

from PIL import Image
from PIL import PngImagePlugin
import json
import os

from library import ribbonBuilder, parseMilpac


def getOutput():
    # Write ind awards output to JSON file and open it for viewing
    print("Enter milpac ID:")
    inp = input()

    indAwards = parseMilpac(int(inp)).indAwards()

    with open("userTest.json", "w") as f:
        json.dump(indAwards, f, indent=4)     

    output = []
    for val in indAwards:
        if val["count"] >= 1:
            output.append(val["shortName"])

    print(output)

    # webbrowser.open("userTest.json")
    return 0


def rackImage():
    # TODO Prepare script to recieve awards array

    ID = input()
    indAwards = parseMilpac(int(ID)).indAwards()

    ribbons = []
    for val in indAwards:
        if val["count"] >= 1:
            ribbons.append(val["shortName"])
    ribbons.reverse()

    ribbonCount = len(ribbons)

    grid = ribbonBuilder(ribbonCount).setupGrid()
    imgRack = Image.new("RGBA", 
    (
        ribbonBuilder(ribbonCount).rackDimensions()["width"],
        ribbonBuilder(ribbonCount).rackDimensions()["height"]
    ))
    count = 0

    for indx, val in enumerate(ribbons):
        count += 1
        ribbon = Image.open("./media/ribbons/"+str(val)+".gif")
        imgRack.paste(ribbon, (grid[indx][0], grid[indx][1]))

    imgRack.save("Ribbon Rack.png", "PNG")

    webbrowser.open("Ribbon Rack.png")  # NOTE FOR DEBUGGING ONLY

    return 0

rackImage()