'''
The Window class is responible for creating the GUI in Treble. The __init__ method creates the button elements and labels in the Interface.
Also includes helper code for some functionality in the sound class.

Martin Harvey 2018
'''

from Tkinter import Tk, Label, Button
from Sound import * 

class Window:

    def __init__(self, master):
        # Set the window title to "Treble"
        master.title("Treble")

        # Set tr to a null value, tr will contain the sound class object we import a file into later 
        self.tr = None

        '''
        Setting up buttons. They are all assigned to the master widget, and are mostly disabled until a track is opened. 
        Buttons are arranged using the pack layout manager.        
        '''
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

        self.undoButton = Button(master, text = "Undo",
                                command = lambda: sound.undo(self.tr), state = 'disabled')
        self.undoButton.pack()

        self.redoButton = Button(master, text = "Redo", 
                                command = lambda: sound.redo(self.tr), state = 'disabled')
        self.redoButton.pack()

        self.closeButton = Button(master, text = "Close Window",
                                command = master.destroy)
        self.closeButton.pack()

        '''
        durLabel allows the user to see the duration of the track in its current form.
        Whenever a duration changing effect is apllied, the label text is updated.
        '''
        self.durLabel = Label(master, text = "Track Duration: 0s")
        self.durLabel.pack()

    '''
    This is helper code for the mergeTrack funciton in the sound class, this function simply calls the mergeTrack function before updating
    the contents of durLabel, using a getter function in sound for the track duration. 
    '''
    def mergeHelper(self):
        sound.mergeTracks(self.tr)
        self.durLabel['text'] = "Track Duration: " + str(int(sound.checkLength(self.tr))) + "s"

    '''
    gapMergeHelper works in the same way as mergeHelper, but simply calls gapMerge instead. 
    '''
    def gapMergeHelper(self):
        sound.gapMerge(self.tr)
        self.durLabel['text'] = "Track Duration: " + str(int(sound.checkLength(self.tr))) + "s"
        
    '''
    Open creates a new instance of the sound class and it sets the buttons to normal state. Also updates the label to the
    new track duration.
    '''
    def open(self):
        self.tr = sound()
        self.durLabel['text'] = "Track Duration: " + str(int(sound.checkLength(self.tr))) + "s"
        self.revButton['state'] = 'normal'
        self.mergeButton['state'] = 'normal'
        self.gapMergeButton['state'] = 'normal'
        self.saveButton['state'] = 'normal'
        self.repeatButton['state'] = 'normal'
        self.overlayButton['state'] = 'normal'
        self.undoButton['state'] = 'normal'
        self.redoButton['state'] = 'normal'
 

    # Calls repeat function and updates label.
    def repeatHelp(self):
        sound.repeat(self.tr)
        self.durLabel['text'] = "Track Duration: " + str(int(sound.checkLength(self.tr))) + "s"
    # Calls overlay and updates label.
    def overlayTrack(self):
        sound.overlay(self.tr)
        self.durLabel['text'] = "Track Duration: " + str(int(sound.checkLength(self.tr))) + "s"



