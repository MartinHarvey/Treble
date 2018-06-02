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

        self.mergeButton = Button(master, text="Gapless Merge",
                                command = lambda: Window.mergeHelper(self), state = 'disabled')
        self.mergeButton.pack()

        self.gapMergeButton = Button(master, text = "Merge with Gap",
                                command = lambda: Window.gapMergeHelper(self), state = 'disabled')
        self.gapMergeButton.pack()

        self.repeatButton = Button(master, text = "Repeat Track",
                                command = lambda: Window.repeatHelp(self), state = 'disabled')
        self.repeatButton.pack()

        self.overlayButton = Button(master, text = "Overlay Two Tracks",
                                command = lambda: Window.overlayTrack(self), state = 'disabled')
        self.overlayButton.pack()

        self.saveButton = Button(master, text="Save Track",
                                command = lambda: sound.save(self.tr), state = 'disabled') 
        self.saveButton.pack()

        self.durLabel = Label(master, text = "Track Duration: 0s")
        self.durLabel.pack()

    def mergeHelper(self):
        sound.mergeTracks(self.tr)
        self.durLabel['text'] = "Track Duration: " + str(int(sound.checkLength(self.tr))) + "s"

    def gapMergeHelper(self):
        sound.gapMerge(self.tr)
        self.durLabel['text'] = "Track Duration: " + str(int(sound.checkLength(self.tr))) + "s"
        

    def open(self):
        self.tr = sound()
        self.durLabel['text'] = "Track Duration: " + str(int(sound.checkLength(self.tr))) + "s"
        self.revButton['state'] = 'normal'
        self.mergeButton['state'] = 'normal'
        self.gapMergeButton['state'] = 'normal'
        self.saveButton['state'] = 'normal'
        self.repeatButton['state'] = 'normal'
        self.overlayButton['state'] = 'normal'
 

    def repeatHelp(self):
        sound.repeat(self.tr)
        self.durLabel['text'] = "Track Duration: " + str(int(sound.checkLength(self.tr))) + "s"
    
    def overlayTrack(self):
        sound.overlay(self.tr)
        self.durLabel['text'] = "Track Duration: " + str(int(sound.checkLength(self.tr))) + "s"



