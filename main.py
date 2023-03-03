import os
import tkinter as tk
from tkinter import *  # tkinter package for GUI purposes
from tkinter import filedialog  # tkinter filedialog package

# Gets file name from file explorer
def file_selection():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select file",
                                          filetypes = (("Adobe Acrobat Document","*.pdf*"),("Microsoft Word Document","*.docx*"),("Microsoft Excel Worksheet","*.xlsx"),("all files","*.*"))
                                          )


# file selection gui for the window and browse file button
def file_select_gui(file_selection):
    window = Tk()  # makes window
    window.geometry("500x500")  # Window size
    window.config(background = "white")  # window background color

    button_file_browse = Button(window, text = "Browse Files", command = file_selection) # file browse button
    button_file_browse.grid(column = 1, row = 2) # file browse button position

    window.mainloop() # waits for user to finish selecting file

if __name__ == '__main__':
    file_select_gui(file_selection) # calling file selection gui function

# function to scrape data from file (sujay's job)


