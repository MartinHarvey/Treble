
from pydub import AudioSegment
from Tkinter import Tk, Label, Button
import tkFileDialog

class sound:
    def __init__(self):
        self.filePath = tkFileDialog.askopenfilename(initialdir = "/home/", title = "What file do you want to import?", filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
        self.track = AudioSegment.from_mp3(self.filePath)
    
    def save(self):
        save_path = tkFileDialog.asksaveasfilename(initialdir = "/home/", title = "Where do you want to save the modified file?")
        self.track.export(save_path, bitrate = "320k",format = "mp3")

    def reverse(self):
        self.track = self.track.reverse()

    def checkLength(self):
        return self.track.duration_seconds
    
    def mergeTracks(self):
        self.filePath = tkFileDialog.askopenfilename(initialdir = "/home/", title = "What file do you want to import?", filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
        self.mergeTrack = AudioSegment.from_mp3(self.filePath)
        self.track = self.track + self.mergeTrack

    def gapMerge(self):
        self.filePath = tkFileDialog.askopenfilename(initialdir = "/home/", title = "What file do you want to import?", filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
        self.mergeTrack = AudioSegment.from_mp3(self.filePath)
        self.track = self.track + AudioSegment.silent(duration = 10000) + self.mergeTrack

    def repeat(self):
        self.track = self.track * 2

    def overlay(self):
        self.filePath = tkFileDialog.askopenfilename(initialdir = "/home/", title = "What file do you want to import?", filetypes = (("mp3 files","*.mp3"),("all files","*.*")))
        self.overlayTrack = AudioSegment.from_mp3(self.filePath)
        self.track = self.track.overlay(self.overlayTrack)