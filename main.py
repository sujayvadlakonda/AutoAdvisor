import os
import sys
import tkinter as tk
from tkinter import *  # tkinter package for GUI purposes
from tkinter import ttk, filedialog, messagebox as mbox
from tkinter.messagebox import showinfo


# Opens file and returns if it's successful or not
def open_file(file_path):
    # Opens file in read-only mode
    if file_path:
        with open(file_path, "r") as f:
            return TRUE
    else:
        return FALSE


# Gets file name from file path
def get_filename(file_path):
    filename = os.path.basename(file_path)
    return filename


# Gets file path of chosen file selected from file explorer and opens it
def file_selection():
    pdf = "Adobe Acrobat Document"
    word_doc = "Microsoft Word Document"
    excel_sheet = "Microsoft Excel Worksheet"
    file_explorer = "/"  # path start for windows
    file_err_msg = "File could not be opened."

    # Check's if computer is macOS
    if os.name == 'posix':
        file_explorer = "\\"

    # opens Windows File Explorer and gets file path
    file_path = filedialog.askopenfilename(initialdir=file_explorer, title="Select file",
                                           filetypes=(("All Files", "*.*"), (pdf, "*.pdf*"),
                                                      (word_doc, "*.docx*"), (excel_sheet, "*.xlsx")))

    file_status = open_file(file_path)  # calls function to open file

    if file_status:
        # Displays name of file that user selected and opened
        showinfo(
            title="File Selected",
            message="File Selected: " + get_filename(file_path)
        )
    else:
        mbox.showerror("Error", file_err_msg)  # failed opening file message box


# file selection gui for the window and browse file button
def file_select_gui(window):
    style = ttk.Style(window)
    style.configure("BW.TLabel", font=("Roboto", 15), foreground="black", background="white")
    style.configure("GWSmall.TLabel", font=("Roboto", 12), foreground="Gray", background="white")
    style.configure("BWSmall.TLabel", font=("Roboto", 12), foreground="Blue", background="white")

    # Upload File text label and design
    lbl_upload = ttk.Label(text="Upload File", style="BW.TLabel")
    lbl_upload.pack(pady=30)  # text padding
    lbl_upload = ttk.Label(text="Select a file (e.g. transcript) to upload:", style="GWSmall.TLabel")
    lbl_upload.pack(pady=10)  # text padding

    # Button to open Window's File Explorer and design
    style.theme_names()
    current_theme = style.theme_use("vista")
    btn_file_browse = ttk.Button(
        window,
        text="Browse Files",
        value=current_theme,
        command=file_selection
    )
    btn_file_browse.pack(side=TOP, pady=20)  # button padding


# Sets up application window
def window_gui():
    window_name = "Degree Plan and Audit Tool"
    window_size = "700x500+270+25"
    window_color = "white"

    window = tk.Tk()  # makes a tkinter frame instance
    window.config(background=window_color)  # Window background color
    window.geometry(window_size)  # Window size
    window.title(window_name)  # Window name
    #icon = PhotoImage(file="./images/project_icon.png")
    #window.iconbitmap(TRUE,icon)  # Window icon

    file_select_gui(window)  # file selection window gui

    window.mainloop()  # keeps window open until exited


def main():
    window_gui()


if __name__ == '__main__':
    main()

# I'll remove these side comments later
# adding "file_path = file_selection()" in file_select_gui() causes file explorer to open before the button is clicked
# adding "return file_path" in file_selection() causes file explorer to open before the button is clicked
# don't put () after button commands or the button will activate before you press it
# ask sujay how they want to connect their code to mine

#  put (tkinter window gui) in a sep Window class in a sep file w/ mainloop function exposed
#  BrowseFileButton class w/ file_selection function in a separate file
#  pulled-out constants
#  show file name, + upload file page pic/outline look nice
#  add a prev + next button that goes to next window page that looks nice
#  add homepage nice looking degree plan and audit tool label, and "+ Start" button, that goes to upload file page

#  vista or default
#  style = ttk.Style(self) and ttk.Label(self, text="", style="chosen_name.TLabel")
#  labelName["text"] = filename
