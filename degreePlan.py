import tkinter as tk
from tkinter import *
from tkinter import ttk


class DegreePlanPage(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller

        self.style = ttk.Style(self)
        self.style.configure("BlckBorder.TFrame", borderwidth=5, background="white", relief=SOLID, height=60, width=70)
        self.style.configure("BlSmall.TLabel", font=("Roboto", 14), foreground="#107896", background="white")

        # Frame outline design
        frame = ttk.Frame(self, style="BlckBorder.TFrame")
        frame["padding"] = (5, 0, 5, 0)  # adjusts inner padding to fit text
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        frame.grid(column=0, row=0, sticky="nsew", columnspan=5, pady=(50, 0))  # keeps pages bundled in same location

        # Text label and design
        lbl_upload = ttk.Label(frame, text="This is a text label example", style="BlSmall.TLabel")
        lbl_upload.grid(column=1, row=0, columnspan=1, padx=30, pady=5)  # text padding

        # Previous page button
        prev_btn = ttk.Button(
            frame,
            text="<< Previous",
            command=lambda: self.controller.show_frame("UploadFilePage")
        )
        prev_btn.grid(column=0, row=2, columnspan=1, sticky="sw", pady=(20, 20))  # button padding

        # Next page button and design
        # next_btn = ttk.Button(frame,text="Next >>",command=lambda: controller.show_frame("ClassNameOfNextPgHere"))
        # next_btn.grid(column=2, row=2, columnspan=1, sticky="se", pady=(20, 20))  # button padding

    # note to developers:
    # This file is just a template for whoever is working on the GUI for the Degree Plan part of the project
    # (it's not an official format, so feel free to modify)
    # if you want to your next/previous page button to work:
        # Add to the top of the degreeApp.py file: from insertYourFileNameHere import insertYourClassNameHere
        # In the degreeApp.py file, add your file's class name to the () in the For Loop
        # In the button's command section, make sure the class name is enclosed in ""
