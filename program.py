import webbrowser  # NOTE FOR DEBUGGING ONLY

from PIL import Image
import json

from library import ribbonBuilder, parseMilpac


def getOutput():
    # Write ind awards output to JSON file and open it for viewing
    with open("userTest.json", "w") as f:
        json.dump(parseMilpac(446).indAwards(), f, indent=4)     
    webbrowser.open("userTest.json")
    return 0


def rackImage():
    # TODO Prepare script to recieve awards array
    ribbonCount = int(input())

    grid = ribbonBuilder(ribbonCount).setupGrid()
    imgRack = Image.new("RGBA", (ribbonBuilder(ribbonCount).rackDimensions()[
                        "width"], ribbonBuilder(ribbonCount).rackDimensions()["height"]))

    testImg = Image.open("./testRibbons/1.png")

    count = 0
    for ribbon in grid:
        count += 1
        # TODO Fix file name when preparing script
        testImg = Image.open("./testRibbons/"+str(count)+".png")
        imgRack.paste(testImg, (ribbon[0], ribbon[1]))

    imgRack.save("Ribbon Rack.png", "PNG")

    webbrowser.open("Ribbon Rack.png")  # NOTE FOR DEBUGGING ONLY

    return 0