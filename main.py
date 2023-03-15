import os
import sys
import tkinter as tk
from tkinter import *  # tkinter package for GUI purposes
from tkinter import ttk, filedialog, messagebox as mbox
from tkinter.messagebox import showinfo


# Opens file and displays an error message if it fails
def open_file(file_name):
    file_err_msg = "File not opened or could not be opened."

    # Opens file in read-only mode
    try:
        with open(file_name, "r") as f:
            # Displays selected file name to user
            showinfo(
                title="Selected File",
                message="Selected file: "+get_filename(file_name)
            )
    except:
        mbox.showerror("Error", file_err_msg)  # failed opening file message box

# Gets file name from file path
def get_filename(file_name):
    filename = os.path.basename(file_name)
    return filename

# Gets file path of chosen file selected from file explorer
def file_selection():
    pdf = "Adobe Acrobat Document"
    word_doc = "Microsoft Word Document"
    excel_sheet = "Microsoft Excel Worksheet"
    file_explorer = "/"  # path start for windows
    finder = "\\"  # path start for mac OS

    # opens Windows File Explorer and gets file path
    file_name = filedialog.askopenfilename(initialdir=file_explorer, title="Select file",
                                           filetypes=(("All Files", "*.*"), (pdf, "*.pdf*"),
                                                      (word_doc, "*.docx*"), (excel_sheet, "*.xlsx")))

    open_file(file_name)  # calls function to open file


# file selection gui for the window and browse file button
def file_select_gui(window):
    # Upload File text label and design
    lbl_upload = Label(
        window,
        text="Upload File",
        font="Roboto 15",
        width=100,
        height=4,
        fg="black",
        bg="white"
    )
    lbl_upload.pack(pady=10)  # text padding

    # Button to open Window's File Explorer and design
    btn_file_browse = Button(
        window,
        text="Browse Files",
        command=file_selection
    )
    btn_file_browse.pack(side=TOP, pady=20)  # button padding


# Sets up application window
def window_gui():
    window_name = "Degree Plan and Audit Tool"
    window_size = "700x500"
    window_color = "white"

    window = Tk()  # makes a tkinter frame instance Window
    window.config(background=window_color)  # Window background color
    window.geometry(window_size)  # Window size
    window.title(window_name)  # Window name

    file_select_gui(window)  # file selection window gui

    window.mainloop()  # keeps window open until exited


def main():
    window_gui()


if __name__ == '__main__':
    main()
