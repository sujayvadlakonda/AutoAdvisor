import tkinter as tk
from tkinter import *
from tkinter import ttk


class DegreePlanPage(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller  # allows for switching between application pages

        ## Trouble shooting
        print('Testing degreePlan') 
        ## Trouble shooting


        # Handles the gui of the Degree Plan page
        self.style = ttk.Style(self)
        self.style.configure("BlckBorder.TFrame", borderwidth=5, background="white", relief=SOLID, height=60, width=70)
        self.style.configure("BlSmall.TLabel", font=("Roboto", 14), foreground="#107896", background="white")

        # Frame outline and design
        frame = ttk.Frame(self, style="BlckBorder.TFrame")
        frame["padding"] = (5, 0, 5, 0)  # adjusts inner padding to fit text
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        frame.grid_columnconfigure(3, weight=1)
        frame.grid(column=0, row=0, sticky="nsew", columnspan=5, pady=(10, 0))  # keeps pages bundled in same location

        # Previous Page button and design
        prev_btn = ttk.Button(
            frame,
            text="<< Previous",
            command=lambda: self.controller.show_frame("UploadFilePage")
        )
        prev_btn.grid(column=0, row=1, columnspan=1, sticky="sw", pady=(10, 20))  # button padding

        # Text label and design
        lbl_report = ttk.Label(frame, text="Generate Audit Report:", style="BlSmall.TLabel")
        lbl_report.grid(column=1, row=1, columnspan=1, sticky="s", padx=5, pady=10)  # text padding

        # Button to direct user to generate Audit Report and design
        next_btn = ttk.Button(
            frame,
            text="Yes",
            command=lambda: controller.show_frame("AuditReportPage")
        )
        next_btn.grid(column=2, row=1, columnspan=1, sticky="s", pady=(10, 20))  # button padding

        # Button to direct user to go back to homepage
        homepage_btn = ttk.Button(
            frame,
            text="No",
            command=lambda: self.controller.show_frame("HomepageStart")
        )
        homepage_btn.grid(column=3, row=1, columnspan=1, sticky="es", pady=(10, 20))  # positioning

    # note to developers:
    # This file is just a template for whoever is working on the GUI for the Degree Plan part of the project
    # modify it as much as you want to, but make sure the user can get to the audit report if they want to
    # if you want to your next/previous page button to work:
        # Add to the top of the degreeApp.py file: from insertYourFileNameHere import insertYourClassNameHere
        # In the degreeApp.py file, add your file's class name to the () in the For Loop
        # In the button's command section, make sure the class name is enclosed in ""
