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
    if file_name:
        with open(file_name, "r") as f:
            # Displays selected file name to user
            showinfo(
                title="Selected File",
                message="Selected file: "+get_filename(file_name)
            )
    else:
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
    style = ttk.Style(window)
    style.configure("BW.TLabel", font=("Roboto", 15), foreground="black", background="white")
    style.configure("GWSmall.TLabel", font=("Roboto", 12), foreground="Gray", background="white")
    style.configure("BWSmall.TLabel", font=("Roboto", 12), foreground="Blue", background="white")

    # Upload File text label and design
    lbl_upload = ttk.Label(text="Upload File", style="BW.TLabel")
    lbl_upload.pack(pady=30)  # text padding
    lbl_upload = ttk.Label(text="Select a file (e.g. transcript) to upload", style="GWSmall.TLabel")
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

# adding "file_name = file_selection()" in file_select_gui() causes file explorer to open before the button is clicked
# adding "return file_name" in file_selection() causes file explorer to open before the button is clicked
# don't put () after button commands or they'll activate before you press the button

#  put (tkinter window gui) in a sep Window class in a sep file w/ mainloop function exposed
#  BrowseFileButton class w/ file_selection function in a separate file
#  pulled-out constants
#  show file name, make buttons+upload file page pic/outline+homepg labels/button look nice
#  add a prev + next button that goes to next window page
#  add homepage with utd ecs+degree plan and audit tool label, and "+ Start" button, that goes to upload file page

#   style = ttk.Style(self) and ttk.Label(self, text="", style="chosenname.TLabel")
# Name of File label and design
#     lbl_filename = Label(
#         window,
#         text="Chosen File",
#         font="Roboto 12",
#         width=50,
#         height=4,
#         fg="black",
#         bg="white"
#     )
#  lbl_filename.configure(text="Chosen File: "+filename)
