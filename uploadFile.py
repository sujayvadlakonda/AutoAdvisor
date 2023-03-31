import os
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog
from tkinter import messagebox as mbox


class UploadFilePage(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller  # Used to control which page is shown

        self.filename = tk.StringVar()  # Holds displayed name of file
        self.file_path = ""

        # Handles the gui of the Upload File page
        style = ttk.Style(self)
        style.configure("BlBord.TFrame", borderwidth=5, background="white", relief=SOLID, height=500, width=700)
        style.configure("picBkgd.TLabel", background="white")
        style.configure("BW.TLabel", font=("Roboto", 20), foreground="black", background="white")
        style.configure("GWSmall.TLabel", font=("Roboto", 14), foreground="Gray", background="white")
        style.configure("BWSmall.TLabel", font=("Roboto", 14), foreground="#107896", background="white")

        # Handles frame expansion when application window is expanded
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Frame outline and design
        frame = ttk.Frame(self, style="BlBord.TFrame")
        frame["padding"] = (5, 0, 5, 0)  # adjusts inner padding to fit text
        frame.grid(column=0, row=0, sticky="nsew", columnspan=5, pady=(20, 0))  # frame placement

        # Handles frame's space distribution
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        frame.grid_rowconfigure(2, weight=1)
        frame.grid_columnconfigure(3, weight=1)
        frame.grid_rowconfigure(3, weight=1)
        frame.grid_columnconfigure(4, weight=1)
        frame.grid_rowconfigure(4, weight=1)
        frame.grid_columnconfigure(5, weight=1)
        frame.grid_rowconfigure(5, weight=1)
        frame.grid_rowconfigure(6, weight=1)

        # Decorative Image label and design
        doc_upload_photo = tk.PhotoImage(file=r"./images/upload_file.png")
        lbl_image = ttk.Label(
            frame,
            image=doc_upload_photo,
            style="picBkgd.TLabel"
        )
        lbl_image.doc_upload_photo = doc_upload_photo  # Required image reference needed for image to show up
        lbl_image.grid(column=1, row=0, sticky="n", columnspan=3, pady=(10, 0))  # positioning

        # Upload File text label and design
        lbl_upload = ttk.Label(frame, text="Upload File", style="BW.TLabel")
        lbl_upload.grid(column=2, row=1, columnspan=1, pady=(5, 5))  # positioning

        # subtext label and design
        lbl_upload_instruct = ttk.Label(frame, text="Click the button to select a file to upload", style="GWSmall.TLabel")
        lbl_upload_instruct.grid(column=1, row=2, columnspan=3, pady=(10, 0))  # positioning

        # Window's File Explorer button and design
        btn_file_browse = ttk.Button(
            frame,
            text="Browse Files",
            command=self.file_selection
        )
        btn_file_browse.grid(column=2, row=3, columnspan=1, pady=(15, 5))  # positioning

        # file name (not file path) text label and design
        self.file_name = ttk.Label(frame, textvariable=self.filename, style="BWSmall.TLabel")
        self.file_name.grid(column=1, row=4, sticky="ew", columnspan=5, padx=(0, 5), pady=(10, 10))  # positioning

        # Previous page button and design
        prev_btn = ttk.Button(
            frame,
            text="<< Previous",
            command=lambda: self.controller.show_frame("HomepageStart")
        )
        prev_btn.grid(column=0, row=5, sticky="sw", columnspan=1, padx=(5, 0), pady=(10, 20))  # positioning

        # Next page button and design
        next_btn = ttk.Button(
            frame,
            text="Next >>",
            command=lambda: self.controller.show_frame("DegreePlanPage")
        )
        next_btn.grid(column=5, row=5, sticky="es", columnspan=1, padx=(0, 5), pady=(10, 20))  # positioning

    # Opens file in read-only mode and returns if it's successful or not
    def open_file(self):
        if self.file_path:
            with open(self.file_path, "r") as f:
                return True
        else:
            return False

    # Sets file path object
    def set_filepath(self, file_path):
        self.file_path = file_path

    # Gets file path of file selected from file explorer by the user and opens it
    def file_selection(self):
        pdf = "Adobe Acrobat Document"
        word_doc = "Microsoft Word Document"
        excel_sheet = "Microsoft Excel Worksheet"
        json = "JavaScript Object Notation File"
        file_explorer = "\\"  # path start for windows
        file_err_msg = "File could not be opened or was not chosen."

        # opens Windows File Explorer and gets file path of the selected file
        file_path = filedialog.askopenfilename(initialdir=file_explorer, title="Open",
                                               filetypes=(("All Files", "*.*"), (pdf, "*.pdf*"),
                                                          (word_doc, "*.docx*"), (excel_sheet, "*.xlsx"),
                                                          (json, ".json")))

        self.set_filepath(file_path)  # sets file path as instance variable/object

        file_status = self.open_file()  # calls function to open file

        # Displays name of file that user selected and opened
        if file_status:
            file_name = "Uploaded File: " + os.path.basename(self.file_path)
            self.filename.set(file_name)
        else:
            mbox.showerror("Error", file_err_msg)  # failed opening file message box

    # Gets file path object/instance variable
    def get_filepath(self):
        return self.file_path
