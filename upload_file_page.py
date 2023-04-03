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
        style.configure("BlBord.TFrame", background="#f8f8ff")
        style.configure("pic_background.TLabel", background="#f8f8ff")
        style.configure("BW.TLabel", font=("Roboto", 20), foreground="black", background="#f8f8ff")
        style.configure("GWSmall.TLabel", font=("Roboto", 14), foreground="Gray", background="#f8f8ff")
        style.configure("BWSmall.TLabel", font=("Roboto", 14), foreground="#107896", background="#f8f8ff")

        # Handles frame expansion when application window is expanded
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Frame outline and design
        frame = ttk.Frame(self, style="BlBord.TFrame")
        frame["padding"] = (5, 0, 5, 0)  # adjusts inner padding to fit text
        frame.grid(column=0, row=0, sticky="nsew", columnspan=6)  # frame placement

        # Handles frame's page space distribution
        for row_index in range(6):
            frame.grid_rowconfigure(row_index, weight=1)
        for col_index in range(6):
            frame.grid_columnconfigure(col_index, weight=1)

        # Decorative Image label and design
        doc_upload_photo = tk.PhotoImage(file=r"./images/upload_file.png")
        lbl_image = ttk.Label(
            frame,
            image=doc_upload_photo,
            style="pic_background.TLabel"
        )
        lbl_image.doc_upload_photo = doc_upload_photo  # image reference needed for image to load
        lbl_image.grid(column=1, row=0, columnspan=5, pady=(10, 0))  # positioning

        # Upload File text label and design
        lbl_upload = ttk.Label(frame, text="Upload File", style="BW.TLabel")
        lbl_upload.grid(column=2, row=1, columnspan=3, padx=(100, 0), pady=(5, 5))  # positioning

        # subtext label and design
        upload_instruct = "Click the button to select a file to upload"
        lbl_upload_instruct = ttk.Label(frame, text=upload_instruct, style="GWSmall.TLabel")
        lbl_upload_instruct.grid(column=1, row=2, columnspan=5, pady=(10, 0))  # positioning

        # Window's File Explorer button and design
        btn_file_browse = ttk.Button(
            frame,
            text="Browse Files",
            command=self.file_selection
        )
        btn_file_browse.grid(column=2, row=3, columnspan=3, padx=(100, 0), pady=(15, 5))  # positioning

        # file name (not file path) text label and design
        self.file_name = ttk.Label(frame, textvariable=self.filename, style="BWSmall.TLabel")
        self.file_name.grid(column=0, row=4, columnspan=6, padx=(0, 5), pady=(10, 10))  # positioning

        # Previous page button and design
        prev_btn = ttk.Button(
            frame,
            text="<< Previous",
            command=lambda: self.controller.show_frame("HomepageStart")
        )
        prev_btn.grid(column=0, row=5, sticky="sw", columnspan=1, padx=(5, 0), pady=(10, 20))  # positioning

        # Next page button that goes to degree_plan_page.py (the page where the user makes a student object) and design
        next_btn = ttk.Button(
            frame,
            text="Make New Degree Plan",
            command=lambda: self.controller.show_frame("DegreePlanPage")
        )
        next_btn.grid(column=5, row=5, sticky="es", columnspan=1, padx=(0, 5), pady=(10, 20))  # positioning

        # Next page button that goes to degree_plan_report_page.py (the editing degree plan page) and design
        next_btn = ttk.Button(
            frame,
            text="Edit Existing Degree Plan",
            command=lambda: self.controller.show_frame("DegreePlanReportPage")
        )
        next_btn.grid(column=6, row=5, sticky="es", columnspan=1, pady=(10, 20))  # positioning

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
        file_types = [("All Files", "*.*"), (pdf, "*.pdf*"), (word_doc, "*.docx*"),
                      (excel_sheet, "*.xlsx"), (json, ".json")]

        # opens Windows File Explorer and gets file path of the selected file
        file_path = filedialog.askopenfilename(initialdir=file_explorer, title="Open", filetypes=file_types)

        self.set_filepath(file_path)  # sets file path as instance variable/object

        file_status = self.open_file()  # calls function to open file

        # Displays name of file that user selected and opened
        if file_status:
            file_name = "Uploaded File: " + os.path.basename(self.file_path)
            self.filename.set(file_name)
        else:
            mbox.showerror("Error", file_err_msg)  # File not opened message box alert

    # Gets file path object/instance variable
    def get_filepath(self):
        return self.file_path
