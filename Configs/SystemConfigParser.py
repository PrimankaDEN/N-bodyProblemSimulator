__author__ = 'PrimankaDEN'
from ConfigParser import *

from Utils.Vector2 import *


class SystemConfigParser:
    win_width = 0
    win_height = 0
    starsNum = 0
    winMiddle = Vector2(0, 0)
    starsColors = []

    def __init__(self, configName):
        self._configName = configName
        self.parser = ConfigParser()

        self.win_width = int(self.parser.read["System"]["WIN_WIDTH"])
        self.win_height = int(self.parser.read["System"]["WIN_HEIGHT"])
        self.starsNum = int(self.parser.read["System"]["STARS_NUMBER"])
        self.starsColors = self.parser.read["System"]["STARS_COLOR"]

        sys = self.config()
        i = sys.get