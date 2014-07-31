__author__ = 'PrimankaDEN'

from Tkinter import *
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
file_menu.add_comand(label="Save pattern as")
file_menu.add_separator()
file_menu.add_command(label="Quit", command=root.destroy)

edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo")
edit_menu.add_separator()
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste", state=DISABLED)

frame = Frame(root)
frame.grid()

#Start button
startBtn = Button(frame, text="Resume/Pause")
def resumeBtnClicked(event):
    print "Start/Stop button"
    if (GameController.isStarted()):
        GameController.pause()
    else:
        GameController.resume()
startBtn.bind("<Button-1>", resumeBtnClicked)
startBtn.grid(row=1, column=0)

#Add object button
addObjBtn= Button(frame,text="Start")
def startBtnClicked(event):
    print "addObjBtnClicked"
    GameController.start()
addObjBtn.bind("<Button-1>", startBtnClicked)
addObjBtn.grid(row=0,column=0)

#Add object button
addObjBtn= Button(frame,text="Add object")
def addObjBtnClicked(event):
    print "addObjBtnClicked"
addObjBtn.bind("<Button-1>", addObjBtnClicked)
addObjBtn.grid(row=2,column=0)

#

lbl = Label(frame, text="Label")
lbl.grid(row=0, column=1)

txt = Text(frame, width=30, height=6)
txt.grid(row=1, column=3)
txt.insert(AtInsert(), "Text. " * 20)

cbtn = Checkbutton(frame, text="Checkbutton")
cbtn.grid(row=2, column=3)

lst = Listbox(frame, height=4, bg="white")
lst.grid(row=1, column=1)
lst.insert('end', "Item 1")
lst.insert('end', "Item 2")

radioframe = Frame(frame, relief=RAISED, borderwidth=2)
radioframe.grid(row=2, column=1, rowspan=3)

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
