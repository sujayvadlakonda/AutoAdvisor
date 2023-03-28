import tkinter as tk
from tkinter import *
from tkinter import ttk
from uploadFile import UploadFile


class Homepage(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller

        # Handles the gui and function of the application homepage
        self.style = ttk.Style(self)
        self.style.configure("BlckBord.TFrame", borderwidth=5, background="white", relief=SOLID, height=60, width=70)
        self.style.configure("PW.TLabel", font=("Segoe print", 30), foreground="#0032A0", background="white")
        self.style.configure("GrySmall.TLabel", font=("Bookman Old Style,", 14), foreground="Gray", background="white")

        # Frame outline design
        frame = ttk.Frame(self, style="BlckBord.TFrame")
        frame["padding"] = (5, 0, 5, 0)  # adjusts inner padding to fit text
        frame.pack(fill=BOTH, expand=False, pady=(50, 0))  # frame padding

        #    container.grid_rowconfigure(0, weight=1)
        #     container.grid_columnconfigure(0, weight=1)
        #     frame.grid(row=0, column=0, sticky="nsew")  # keeps pages bundled in the same location

        # Homepage title label and design
        lbl_upload = ttk.Label(frame, text="Degree Plan and Audit Tool", style="PW.TLabel")
        lbl_upload.pack(side=TOP, padx=30, pady=(30, 10))  # text padding

        # subtext label and design
        lbl_upload = ttk.Label(frame, text="Press the Start Button to Begin", style="GrySmall.TLabel")
        lbl_upload.pack(fill=NONE, expand=False, padx=20, pady=10)  # text padding

        # Homepage Start button and design
        self.start_btn = tk.Button(
            frame,
            text=" + Start ",
            font=("Segoe UI", 16),
            foreground="white",
            background="#553980",
            bd="5",
            height="0",
            width="10",
            relief="raised",
            command=lambda: controller.show_frame(UploadFile)
        )
        self.start_btn.pack(side=TOP, pady=(20, 20))  # button padding
