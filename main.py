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

    # Displays name of file that user selected and opened or error message
    if file_status:
        filename = get_filename(file_path)
        showinfo(
            title="File Selected",
            message="File Selected: " + filename
        )
    else:
        mbox.showerror("Error", file_err_msg)  # failed opening file message box


# file selection gui for the window and browse file button
def file_select_gui(window):
    style = ttk.Style(window)
    style.configure("BW.TLabel", font=("Roboto", 15), foreground="black", background="white")
    style.configure("GWSmall.TLabel", font=("Roboto", 12), foreground="Gray", background="white")
    style.configure("BWSmall.TLabel", font=("Roboto", 12), foreground="Blue", background="white")
    style.configure("BlBord.TFrame", borderwidth=5, background="white", relief=SOLID, height=60, width=70)
    style.configure("picBkgd.TLabel", background="white")

    # Frame outline design
    frame = ttk.Frame(window, style="BlBord.TFrame")
    frame['padding'] = (5, 0, 5, 0)  # adjusts inner padding to fit text
    frame.pack(fill=NONE, expand=False, pady=20)  # frame padding

    # Decorative Image label and design
    doc_up_photo = tk.PhotoImage(file=r"./images/no_bkgd_file.png")
    lbl_image = ttk.Label(
        frame,
        image=doc_up_photo,
        style="picBkgd.TLabel"
    )
    lbl_image.doc_up_photo = doc_up_photo  # image reference to display image
    frame['padding'] = (200, 0, 200, 0)  # adjusts inner padding for visual aesthetic
    lbl_image.pack(side=TOP, pady=(20, 10))  # padding

    # Upload File text label and design
    lbl_upload = ttk.Label(frame, text="Upload File", style="BW.TLabel")
    lbl_upload.pack(pady=10)  # text padding
    lbl_upload = ttk.Label(frame, text="Click the button to select a file to upload: ", style="GWSmall.TLabel")
    lbl_upload.pack(pady=10)  # text padding

    # Open Window's File Explorer button and design
    btn_file_browse = ttk.Button(
        frame,
        text="Browse Files",
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
    icon = tk.PhotoImage(file="./images/project_icon.png")
    window.iconphoto(FALSE, icon)  # window icon logo

    file_select_gui(window)  # file selection window gui

    window.mainloop()  # keeps window open until exited


def main():
    window_gui()


if __name__ == '__main__':
    main()

# adding "file_path = file_selection()" in file_select_gui() causes file explorer to open before the button is clicked
# adding "return file_path" in file_selection() causes file explorer to open before the button is clicked
# don't put () after button commands or the button will activate before you press it
# ask sujay how they want to connect their code to mine since he has a mac

#  put (tkinter window gui) in a sep Window class in a sep file w/ mainloop function exposed
#  BrowseFileButton class w/ file_selection function in a separate file
#  pulled-out constants, 
#  show file name, import file thing
#  add a prev + next button that goes to next window page that looks nice
#  add homepage nice looking degree plan and audit tool label, and "+ Start" button, that goes to upload file page

#  style = ttk.Style(self) and ttk.Label(self, text="", style="chosen_name.TLabel")
#  add self. to filename variable to access it any within a class
# from fileName import className
#  labelName["text"] = filename # changes parameter without needing config after value already set
#  current_theme = style.theme_use("vista"), vista/default
# background color e.g.: "#2780e3"

