import os
import sys
import tkinter as tk
from tkinter import *  # tkinter package for GUI purposes
from tkinter import filedialog  # tkinter filedialog package

# Gets file name from file explorer and opens it
def file_selection():
    file_name = filedialog.askopenfilename(initialdir="/",
                                          title="Select file",
                                          filetypes=(("All Files","*.*"),("Adobe Acrobat Document","*.pdf*"),("Microsoft Word Document","*.docx*"),("Microsoft Excel Worksheet","*.xlsx")))

    # Opens file in read-only mode just in case file_name doesn't do so
    try:
        fp=open(file_name,"r")  # opens file in read-only mode
        fp.close()  # closes file
        print("User selected the file: " + file_name) # prints in terminal the path of opened file
    except:
        print("File count not be opened ")  # prints error message of file couldn't be opened
        print(sys.exit())  # exits system

# file selection gui for the window and browse file button
def file_select_gui(file_selection):
    window = Tk()  # makes Window
    window.config(background="white")  # Window background color
    window.geometry("700x500")  # Window size
    window.title('Degree Plan and Audit Tool') # Window name

    button_file_browse = Button(window, text="Browse Files", command=file_selection)  # File Browse button to open file
    button_file_browse.pack(side = 'top') # places File Browse button near the top of window

    window.mainloop()  # waits for user to finish selecting file

if __name__ == '__main__':
    file_select_gui(file_selection) # calling file selection gui function


# function to scrape data from file (sujay's job)


