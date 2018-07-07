'''
Treble main driver code. 

Creates an instance of the window class, which in turns create a sound instance.

Martin Harvey 2018
'''
# import window class, and basic Tkinter functionality
import window
from Tkinter import Tk

# Creates a root tk applet and sets it to be an instance of class window from window.py
if __name__ == "__main__":
    root = Tk()
    wind = window.Window(root)
    root.mainloop()
