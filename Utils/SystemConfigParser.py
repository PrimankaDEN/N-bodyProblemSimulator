__author__ = 'PrimankaDEN'
from ConfigParser import *

from Vector2 import *


class SystemConfigParser:
    win_widht=0
    win_heigth =0
    starsNum=0
    winMiddle = Vector2(0,0)
    starsColors = []

    def __init__(self, configName):
        self._configName = configName
        self.parser=SafeConfigParser()

        self.win_widht = self.parser.read("System", "WIN_WIDHT")
        self.win_heigth = self.parser.read("System", "WIN_HEIGTH")
        self.starsNum = self.parser.read("System", "STARS_NUMBER")
        self.starsColors = self.parser.read("System", "STARS_COLOR")

        sys = self.config()
        i = sys.get