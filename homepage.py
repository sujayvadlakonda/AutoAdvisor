import tkinter as tk
from tkinter import *
from tkinter import ttk
from degreeApp import DegreeApp

class Homepage(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.pack(fill=BOTH, expand=True) # assigns ttk.Frame to root application window
        self.homepage_gui()

    # Handles the gui and function of the application homepage
    def homepage_gui(self):
        self.style = ttk.Style(self)
        self.style.configure("BW.TLabel", font=("Roboto", 30), foreground="black", background="white")
        self.style.configure("BlBord.TFrame", borderwidth=5, background="white", relief=SOLID, height=60, width=70)

        # Frame outline design
        self.frame = ttk.Frame(self, style="BlBord.TFrame")
        self.frame["padding"] = (5, 0, 5, 0)  # adjusts inner padding to fit text
        self.frame.pack(fill=BOTH, expand=False, pady=20)  # frame padding

        # Homepage title label and design
        lbl_upload = ttk.Label(self.frame, text="Degree Plan and Audit Tool", style="BW.TLabel")
        lbl_upload.pack(fill=NONE, expand=False, padx=30, pady=10)  # text padding

        # Homepage Start button and design
        btn_file_browse = ttk.Button(
            self.frame,
            text="+ Start",
            command=self.file_selection
        )
        btn_file_browse.pack(side=TOP, pady=20)  # button padding
