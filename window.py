from pydub import AudioSegment
from Tkinter import Tk, Label, Button, PanedWindow
import tkFileDialog
from Sound import *

class Window:

    def __init__(self, master):
        master.title("Treble")

        self.tr = None

        self.openButton = Button(master, text="Open Track",
                                command = lambda: Window.open(self))
        self.openButton.pack()


        self.revButton = Button(master, text="Reverse Track",
                                command = lambda: sound.reverse(self.tr), state = 'disabled')
        self.revButton.pack()

        self.mergeButton = Button(master, text="Merge Track",
                                command = lambda: Window.mergeHelper(self), state = 'disabled')
        self.mergeButton.pack()

        self.repeatButton = Button(master, text = "Repeat Track",
                                command = lambda: Window.repeatHelp(self), state = 'disabled')
        self.repeatButton.pack()

        self.saveButton = Button(master, text="Save Track",
                                command = lambda: sound.save(self.tr), state = 'disabled') 
        self.saveButton.pack()

        self.durLabel = Label(master, text = "Track Duration: 0s")
        self.durLabel.pack()

    def mergeHelper(self):
        sound.mergeTracks(self.tr)
        self.durLabel['text'] = "Track Duration: " + str(int(sound.checkLength(self.tr))) + "s"

    def open(self):
        self.tr = sound()
        self.durLabel['text'] = "Track Duration: " + str(int(sound.checkLength(self.tr))) + "s"
        self.revButton['state'] = 'normal'
        self.mergeButton['state'] = 'normal'
        self.saveButton['state'] = 'normal'
        self.repeatButton['state'] = 'normal'
 

    def repeatHelp(self):
        sound.repeat(self.tr)
        self.durLabel['text'] = "Track Duration: " + str(int(sound.checkLength(self.tr))) + "s"
    

