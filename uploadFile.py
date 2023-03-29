import os
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog
from tkinter import messagebox as mbox


class UploadFilePage(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller

        self.filename = tk.StringVar()  # Holds displayed name of file
        self.file_path = ""

        # Handles the gui of the Upload File page
        self.style = ttk.Style(self)
        self.style.configure("BlBord.TFrame", borderwidth=5, background="white", relief=SOLID, height=60, width=70)
        self.style.configure("picBkgd.TLabel", background="white")
        self.style.configure("BW.TLabel", font=("Roboto", 20), foreground="black", background="white")
        self.style.configure("GWSmall.TLabel", font=("Roboto", 14), foreground="Gray", background="white")
        self.style.configure("BWSmall.TLabel", font=("Roboto", 14), foreground="#107896", background="white")

        # Frame outline design
        frame = ttk.Frame(self, style="BlBord.TFrame")
        frame["padding"] = (5, 0, 5, 0)  # adjusts inner padding to fit text
        # frame.grid_columnconfigure(0, weight=1)
        # frame.grid_rowconfigure(0, weight=1)
        # frame.grid_columnconfigure(1, weight=1)
        # frame.grid_rowconfigure(1, weight=1)
        # frame.grid_columnconfigure(2, weight=1)
        # frame.grid_rowconfigure(2, weight=1)
        # frame.grid_rowconfigure(3, weight=1)
        # frame.grid_rowconfigure(4, weight=1)
        # frame.grid_rowconfigure(5, weight=1)
        # frame.grid_rowconfigure(6, weight=1)
        # frame.grid(column=0, row=0, sticky="nsew", columnspan=5, pady=(10, 0))  # keeps pages bundled in same location
        frame.pack(fill=BOTH, expand=False)  # frame padding

        # Decorative Image label and design
        doc_upload_photo = tk.PhotoImage(file=r"./images/upload_file.png")
        lbl_image = ttk.Label(
            frame,
            image=doc_upload_photo,
            style="picBkgd.TLabel"
        )
        lbl_image.doc_upload_photo = doc_upload_photo  # Required image reference needed for image to show up
        # lbl_image.grid(column=1, row=0, sticky="n", columnspan=3, pady=(10, 0))  # positioning
        lbl_image.pack(side=TOP, fill=NONE, padx=(20, 0), pady=(5, 0))  # padding

        # Upload File text label and design
        lbl_upload = ttk.Label(frame, text="Upload File", style="BW.TLabel")
        # lbl_upload.grid(column=2, row=1, sticky="ew", columnspan=1, padx=30, pady=(5, 5))  # positioning
        lbl_upload.pack(fill=NONE, expand=False, padx=30)  # text padding

        # subtext label and design
        lbl_upload_instruct = ttk.Label(frame, text="Click the button to select a file to upload: ", style="GWSmall.TLabel")
        # lbl_upload_instruct.grid(column=1, row=2, sticky="ew", columnspan=3, pady=(10, 0))  # positioning
        lbl_upload_instruct.pack(fill=NONE, expand=False, padx=20, pady=(10, 0))  # text padding

        # Window's File Explorer button and design
        btn_file_browse = ttk.Button(
            frame,
            text="Browse Files",
            command=self.file_selection
        )
        # btn_file_browse.grid(column=2, row=3, sticky="n", columnspan=1, pady=(15, 0))  # positioning
        btn_file_browse.pack(side=TOP, pady=(15, 0))  # button padding

        # file name (not file path) text label and design
        self.file_name = ttk.Label(frame, textvariable=self.filename, style="BWSmall.TLabel")
        # self.file_name.grid(column=1, row=4, sticky="ew", columnspan=5, pady=(10, 0))  # positioning
        self.file_name.pack(pady=(10, 0))

        # Previous page button and design
        prev_btn = ttk.Button(
            frame,
            text="<< Previous",
            command=lambda: self.controller.show_frame("HomepageStart")
        )
        # prev_btn.grid(column=0, row=5, sticky="sw", columnspan=1, pady=(5, 20))  # positioning
        prev_btn.pack(pady=(5, 20))  # button padding

        # Next page button and design
        next_btn = ttk.Button(
            frame,
            text="Next >>",
            command=lambda: self.controller.show_frame("DegreePlanPage")
        )
        # prev_btn.grid(column=4, row=5, sticky="es", columnspan=1, pady=(5, 20))  # positioning
        next_btn.pack(pady=(5, 20))  # button padding

    # Opens file in read-only mode and returns if it's successful or not
    def open_file(self):
        if self.file_path:
            with open(self.file_path, "r") as f:
                return True
        else:
            return False

    # Gets file path of file selected from file explorer by the user and opens it
    def file_selection(self):
        pdf = "Adobe Acrobat Document"
        word_doc = "Microsoft Word Document"
        excel_sheet = "Microsoft Excel Worksheet"
        file_explorer = "\\"  # path start for windows
        file_err_msg = "File could not be opened or was not chosen."

        # opens Windows File Explorer and gets file path of the selected file
        self.file_path = filedialog.askopenfilename(initialdir=file_explorer, title="Open",
                                                    filetypes=(("All Files", "*.*"), (pdf, "*.pdf*"),
                                                               (word_doc, "*.docx*"), (excel_sheet, "*.xlsx")))

        file_status = UploadFilePage.open_file(self)  # calls function to open file

        # Displays name of file that user selected and opened
        if file_status:
            file_name = "Uploaded File: " + os.path.basename(self.file_path)
            self.filename.set(file_name)
        else:
            mbox.showerror("Error", file_err_msg)  # failed opening file message box
