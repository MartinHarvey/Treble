'''
Sound.py contains the sound class in the Treble Project. The sound class is responisble for editing AudioSegment objects and
storing them. 

All effects are made using pydub.

Martin Harvey 2018
'''
#Importing modules used to open fileDialog and edit AudioSement 
from pydub import AudioSegment
from Tkinter import Tk, Label, Button
import tkFileDialog

'''
The sound class contains the variable track, which contains a AudioSegment object. This object is where all effects are applied and
contains the user inputed audio file.

sound also contains all code for applying effects to track and getter functions for the window class.
'''
class sound:
    def __init__(self):
        # Open a file using Tkinter's built in filedialog. The dialog allows a .mp3 file to be opened.
        self.filePath = tkFileDialog.askopenfilename(initialdir = "/home/", title = "What file do you want to import?", filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
        # Using pydub, we create a AudioSegment object from the user-chosen .mp3 file. This object is stored in track.
        self.track = AudioSegment.from_mp3(self.filePath)
        # stack and queue are arrays used in the undo/redo functionality. 
        self.queue = []
        self.stack = []
    
    # Using Tkinter to choose a location to save variable track and then exporting track to that location using AudioSegment 
    # as 320kbps mp3 file.
    def save(self):
        # Similar to use of tkfiledialog in __init__ but this time we choose a directory and filename to save track to.
        save_path = tkFileDialog.asksaveasfilename(initialdir = "/home/", title = "Where do you want to save the modified file?", filetypes = (("mp3 files","*.mp3"), ("all files","*.*")))
        # pyDubs export function allows us to output track to the file path specified by the user.
        self.track.export(save_path, bitrate = "320k",format = "mp3")

    
    '''
    reverse allows us to reverse track using pydub. We append the current contents of track to the end of the stack array, this will
    us to revert back.
    '''
    def reverse(self):
        self.stack.append(self.track)
        self.track = self.track.reverse()

    '''
    checkLength is a getter function wich returns the current length of track. This is used by the window class to display the length
    in seconds of track. 
    '''
    def checkLength(self):
        return self.track.duration_seconds
    
    '''
    mergeTracks appends a new file (in AudioSegment type) to the end of track without a gap between the two. A second track is chosen by
    the user in much the same way as opening the first, and a second AudioSegment object is created. Using pyDubs concatenation syntax, we
    merge two tracks together.
    '''
    def mergeTracks(self):
        self.stack.append(self.track)
        self.filePath = tkFileDialog.askopenfilename(initialdir = "/home/", title = "What file do you want to import?", filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
        self.mergeTrack = AudioSegment.from_mp3(self.filePath)
        self.track = self.track + self.mergeTrack

    '''
    gapMerge allows the user to merge two tracks together in the same way as mergeTracks, along with a one second gap between the two tracks
    '''
    def gapMerge(self):
        self.stack.append(self.track)
        self.filePath = tkFileDialog.askopenfilename(initialdir = "/home/", title = "What file do you want to import?", filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
        self.mergeTrack = AudioSegment.from_mp3(self.filePath)
        self.track = self.track + AudioSegment.silent(duration = 10000) + self.mergeTrack

    def repeat(self):
        self.stack.append(self.track)
        self.track = self.track * 2

    # Overlay loads in a new AudioSegment and overlays it with track. Useful if you have two channels of audio I suppose.
    def overlay(self):
        self.stack.append(self.track)
        self.filePath = tkFileDialog.askopenfilename(initialdir = "/home/", title = "What file do you want to import?", filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
        self.overlayTrack = AudioSegment.from_mp3(self.filePath)
        self.track = self.track.overlay(self.overlayTrack)

    '''
    The undo and redo functions depend on the arrays stack and queue. 

    Stack contains the earlier forms of track. When an effect function is called, the follwing code is executed:

            self.stack.append(self.track)
        
    This adds the current track to end of the array, which allows the undo function to revert to this previous
    version of track.

    Queue contains the versions of track you can revert back to after a series of undos. 

    With stack, track and queue, they way versions of track are stored is like this, before the undo function is called:

    ['Old' Versions of track}        curent track   queue
    [stack[0] | stack[1] | stack[3]] [track]        [null]
    
    After the user undos actions:

    ['Old' Versions of track}        curent track   queue
    [stack[0] | stack[1]]            [track]        [queue[0]]

    I hope this helps illustrates how the stack and queue works.

    '''
    def undo(self):
        self.queue.insert(0, self.track)
        self.track = self.stack.pop()
    
    def redo(self):
        self.stack.append(self.track)
        self.track = self.queue[0]
        self.queue.pop(0)
