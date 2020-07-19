# IMPORT FOR GUI
import tkinter as tk
from tkinter import messagebox


# FUNCTION TO SHOW ABOUT MESSAGAE
def about():
    myself="This app is created by Rashandeep Singh.\n Pursuing Computer Science engineering.\nCollege- CCET, PU, Chandigarh "
    return myself

# FUNCTION TO QUIT THE APP
def quiter():
    iExit = tk.messagebox.askyesno("Confirm","Are you sure to exit?") # TO DISPLAY CONFIRM BOX
    if iExit > 0:
        exit()
