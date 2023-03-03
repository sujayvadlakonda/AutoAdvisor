import os
import tkinter as tk
from tkinter import *  # tkinter package for GUI purposes
from tkinter import filedialog  # tkinter filedialog package

# Gets file name from file explorer
def file_selection():
    file_name = filedialog.askopenfilename(initialdir="/",
                                          title="Select file",
                                          filetypes=(("Adobe Acrobat Document","*.pdf*"),("Microsoft Word Document","*.docx*"),("Microsoft Excel Worksheet","*.xlsx"),("all files","*.*")))

# file selection gui for the window and browse file button
def file_select_gui(file_selection):
    window = Tk()  # makes Window
    window.config(background="white")  # Window background color
    window.geometry("700x500")  # Window size
    window.title('Degree Plan and Audit Tool') # Window name

    button_file_browse = Button(window, text="Browse Files", command=file_selection)  # File Browse button
    button_file_browse.pack(side = 'top') # places button near the top of window

    window.mainloop()  # waits for user to finish selecting file

if __name__ == '__main__':
    file_select_gui(file_selection) # calling file selection gui function


# function to scrape data from file (sujay's job)


