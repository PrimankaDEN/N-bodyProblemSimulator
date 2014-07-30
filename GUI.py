__author__ = 'PrimankaDEN'

from Tkinter import *
from game import *
import threading

class StartButton:
    isStarted = False

    def __init__(self):
        self.startBut = Button(root)
        self.startBut["text"] = "Start"
        self.startBut.bind("<Button-1>", self.start)
        self.startBut.pack()

    def start(self, event):
        if self.isStarted:
            self.isStarted = False
            self.startBut["text"] = "Start"
        else:
            t = threading.Thread(target = startMainScreen)
            t.start()

            self.isStarted = True
            self.startBut["text"] = "Pause"



root = Tk()
startBut = StartButton()
root.mainloop()
