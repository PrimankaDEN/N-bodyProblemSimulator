__author__ = 'PrimankaDEN'
from Tkinter import *
from ttk import Combobox

from game import *


class StartButton:
    isStarted = False

    def __init__(self, frame):
        self.startBut = Button(frame)
        self.startBut["text"] = "Start"
        self.startBut.bind("<Button-1>", self.start)
        self.startBut.pack()

    def start(self, event):
        if self.isStarted:
            self.isStarted = False
            self.startBut["text"] = "Start"
        else:
            #t = threading.Thread(target = startMainScreen)
            #t.start()

            self.isStarted = True
            self.startBut["text"] = "Pause"


root = Tk()
root.title("Control central")

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New pattern")
file_menu.add_command(label="Open pattern")
file_menu.add_command(label="Save pattern as")
file_menu.add_separator()
file_menu.add_command(label="Quit", command=root.destroy)

edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo")
edit_menu.add_separator()
edit_menu.add_command(label="Add object")
edit_menu.add_command(label="Delete object")
edit_menu.add_separator()
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste", state=DISABLED)
edit_menu.add_separator()
edit_menu.add_command(label="Properties")

run_menu = Menu(menu)
menu.add_cascade(label="Run", menu=run_menu)
run_menu.add_command(label="Run", command=GameController.start())
run_menu.add_command(label="Pause/Resume", command=GameController.pauseOrResume())
run_menu.add_command(label="Stop", command=GameController.stop())

frame = Frame(root)
frame.grid()

#On/off show path
isPathShownCbtn = Checkbutton(frame, text="Show path")
isPathShownCbtn.grid(row=1, column=4)

#Set delta time
deltaTimeLabel = Label(frame, text="Delta time")
deltaTimeLabel.grid(row=2, column=0)
deltaTimeScale = Scale(frame, orient=HORIZONTAL, length=200, from_=0, to_=100, tickinterval=20, resolution=1)
deltaTimeScale.grid(row=2, column=1)

#Set delay
delayLabel = Label(frame, text="Delay")
delayLabel.grid(row=3, column=0)
delayScale = Scale(frame, orient=HORIZONTAL, length=200, from_=0, to_=100, tickinterval=20, resolution=1)
delayScale.grid(row=3, column=1)

#List of objects
combobox = Combobox(frame, values=["Sun", "Earth", "Moon"], height=3)
combobox.grid(row=1, column = 5)

cbtn = Checkbutton(frame, text="Checkbutton")
cbtn.grid(row=2, column=3)

lst = Listbox(frame, height=4, bg="white")
lst.grid(row=1, column=1)
lst.insert('end', "Item 1")
lst.insert('end', "Item 2")

radioframe = Frame(frame, relief=RAISED, borderwidth=2)
radioframe.grid(row=2, column=2, rowspan=3)

wave = StringVar()
wave.set("1")

radioframe.r1 = Radiobutton(radioframe, text="LW",
                            variable=wave, anchor=W, value="1")
radioframe.r1.pack(fill=X)
radioframe.r2 = Radiobutton(radioframe, text="MW",
                            variable=wave, anchor=W, value="2")
radioframe.r2.pack(fill=X)
radioframe.r3 = Radiobutton(radioframe, text="FM",
                            variable=wave, anchor=W, value="3")
radioframe.r3.pack(fill=X)

pic = Canvas(frame, relief=SUNKEN, bg='white', width=200, height=60)
pic.grid(row=4, column=0)

pic.create_rectangle(2, 2, "30", "30", fill="black")
pic.create_oval(10, 10, 50, 50, fill="white")

lbl2 = Label(frame, text="(Canvas)", bg="white")
pic.create_window(60, 30, window=lbl2)

root.mainloop()
