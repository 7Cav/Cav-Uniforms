import json
import re

import requests
from PIL import Image


class parseMilpac:
    def __init__(self, milpacID):
        html = requests.get("https://7cav.us/rosters/profile?uniqueid="+str(milpacID)).text
        regex = r"awardTitle..(.*)</td>"

        with open("config.json") as f:
            # Get object that contains the config for each award
            self.awardConfig = json.load(f)["awardsOrder"]

        self.milpacAwards = []
        for rawMatch in re.findall(regex, html):
            # Get all award names on the milpac an append it to milpacAwards
            self.milpacAwards.append(rawMatch)

    def indAwards(self):
        '''Builds up award count for individual awards'''

        configAwards = self.awardConfig["individual"]

        for milpacEntry in self.milpacAwards:
            # Loop through each milpac award
            for config in configAwards:
                # Loop through each award in config
                if config["longName"] == milpacEntry:
                    # If milpadEntry is in config, +1 to it's count
                    config["count"] += 1

        return configAwards





class ribbonBuilder:
    def __init__(self, ribNum):
        '''Sets up all grid points nessecary to build a ribbon rack'''

        with open("config.json") as f:
            sizes = json.load(f)["ribbonSizes"]
        self.ribbonWidth = sizes["width"]
        self.ribbonHeight = sizes["height"]
        # How much of a gap there will be between each ribbon, in pixels.
        self.pixelGap = 1
        self.ribNum = ribNum

    def rackDimensions(self):
        '''
        Finds the ribbon rack pixel dimensions.
        Based on how many ribbons will be used.

        :param ribNum: Amount of ribbons on rack.

        :return style: (str) Size style of the ribbon rack, Regular or Large.
        :return width: (int) Ribbon rack pixel width.
        :return height: (int) Ribbon rack pixel height.
        :return rows: (int) Amount of rows on the rack.
        '''
        ribNum = self.ribNum

        ribbonHeight = 27  # Height of an individual ribbon.
        ribbonWidth = 100  # Width of an individual ribbon.

        rows = 0

        if ribNum < 13:  # If there is less than 13 ribbons on the rack
            pixelWidth = (ribbonWidth * 3) + 2
            style = "Regular"

            if (ribNum % 3) == 0:
                rows = ribNum / 3
            else:
                rows = (ribNum // 3) + 1

        else:  # If 13 or more ribbons on the rack
            pixelWidth = (ribbonWidth * 4) + 3
            style = "Large"

            if ribNum <= 14:  # 2 rows of 4 ribbons && 2 row of 3 ribbons
                rows = 4
            elif ribNum <= 17:  # 2 rows of 4 ribbons && 3 rows of 3 ribbons
                rows = 5
            else:  # 2 rows of 4 ribbons && 3 rows of 3 ribbons && ? rows of 2 ribbons
                rows = 5
                ribNum -= 17

                if (ribNum % 2) != 0:
                    ribNum -= (ribNum % 2)
                    rows += 1

                rows += (ribNum / 2)

        pixelHeight = (rows * ribbonHeight) + (rows - 1)

        return {
            "style": style,
            "rows": int(rows),
            "width": int(pixelWidth),
            "height": int(pixelHeight)
        }

    def setupGrid(self):
        '''
        Build an object array of the grid coordinates for all the ribbons.
        Works from position of ribbon 1 (Bottom-Right), and works up
        up from there, in order of precedence of the ribbons.
        '''

        style = self.rackDimensions()["style"]
        rows = self.rackDimensions()["rows"]
        imgHeight = self.rackDimensions()["height"]
        imgWidth = self.rackDimensions()["width"]
        ribCount = self.ribNum

        def regular(rows, imgHeight, imgWidth, ribCount):
            '''Grid builder for rack width of 3 ribbons'''
            grid = []

            for row in range(1, rows + 1):
                if row == 1:
                    # If first row do not shift x up for 1 pixel spacing
                    pixelSpace = 0
                else:
                    # Else accound for 1 pixel spacing between each ribbon
                    pixelSpace += 1

                y = imgHeight - (self.ribbonHeight * row + pixelSpace)

                if ribCount >= 3:
                    xVals = [0, 0 + (101 * 1), 0 + (101 * 2)]
                    xVals.reverse()
                    for x in xVals:
                        grid.append([x, y])
                    ribCount -= 3
                elif ribCount == 2:
                    xVals = [imgWidth // 2 - 101, imgWidth // 2]
                    xVals.reverse()
                    for x in xVals:
                        grid.append([x, y])
                    ribCount -= 2
                elif ribCount == 1:
                    xVals = [imgWidth // 2 - (self.ribbonWidth // 2)]
                    xVals.reverse()
                    for x in xVals:
                        grid.append([x, y])
                    ribCount -= 1

            return grid

        def large(rows, imgHeight, imgWidth, ribCount):
            '''Grid builder for rack width of 4 ribbons'''

            grid = []

            for row in range(1, rows + 1):
                if row == 1:
                    # If first row do not shift x up for 1 pixel spacing
                    pixelSpace = 0
                else:
                    # Else accound for 1 pixel spacing between each ribbon
                    pixelSpace += 1

                y = imgHeight - (self.ribbonHeight * row + pixelSpace)

                xVals = []
                for i in range(1, 4 + 1):  # 4 is the max width, in ribbons, of the large rack
                    xVals.append(imgWidth - (101 * i))
                # xVals = [0, 101, 202, 303] # X values where ribbons will be placed from left to right, factors in 1px spacing.
                # xVals.reverse() # Reverses order due to grid being build on a right to left placement or ribbons

                if row <= 2:  # First two rows, 4 ribbons each
                    for x in xVals:
                        grid.append([x, y])
                    ribCount -= 4
                elif row <= 5:  # Rows 3 to 5, 3 ribbons each
                    for x in xVals[:3]:
                        grid.append([x, y])
                    ribCount -= 3
                else:  # Rows 6 and up, 2 ribbons each
                    if ribCount >= 2:  # If 2 ribbons left
                        for x in xVals[:2]:
                            grid.append([x, y])
                        ribCount -= 2
                    else:  # If one ribbon left
                        for x in xVals[:1]:
                            grid.append([x, y])
                        ribCount -= 1

            return grid

        if style == "Regular":
            return regular(rows, imgHeight, imgWidth, ribCount)
        else:
            return large(rows, imgHeight, imgWidth, ribCount)