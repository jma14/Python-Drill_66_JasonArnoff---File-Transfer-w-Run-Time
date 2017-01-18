# Python:       3.6.0
# Author:       Jason Arnoff
# Purpose:      Tech Academy Drill
#               Python Course - Item 65
#               This program moves files that have been edited
#               in the last 24 hours from one folder to another.
#               User's must be able to browse for the "from"
#               folder and the "to" folder, and initiate the file check.
#               Must track last time the run was executed.
#
#               transfer_recent_main

from tkinter import *
from tkinter import messagebox
import tkinter as ttk
from datetime import *
from datetime import timedelta
import shutil
import os


import transfer_recent_gui
import transfer_recent_func



# Create window for gui
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        # Set master frame size, not resizeable
        self.master = master
        self.master.minsize(500, 260)
        self.master.maxsize(500, 260)

        # Center the window on the screen
        transfer_recent_func.center_window(self, 500, 260)
        self.master.title("Transfer Recently Modified Files")
        self.master.configure(bg="lightgrey")

        # Catch the "X"/Close in the upper corner for windows users
        self.master.protocol("WM_DELETE_WINDOW", lambda: transfer_recent_func.ask_quit(self))

        # Load the gui
        transfer_recent_gui.load_gui(self)

        # Create/Load db for last time program was run
        transfer_recent_func.create_db(self)

        

        










if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
