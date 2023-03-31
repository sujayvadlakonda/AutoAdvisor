import tkinter as tk
from tkinter import *
from tkinter import ttk


class AuditReportPage(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller

        # Handles gui for audit report page
        style = ttk.Style(self)
        style.configure("BlackBord.TFrame", borderwidth=5, background="white", relief=SOLID, height=60, width=70)
        style.configure("BlackSmall.TLabel", font=("Roboto", 14), foreground="#107896", background="white")

        # Handles frame expansion when application window is expanded
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Frame outline design
        frame = ttk.Frame(self, style="BlackBord.TFrame")
        frame["padding"] = (5, 0, 5, 0)  # adjusts inner padding to fit text
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        frame.grid_rowconfigure(2, weight=1)
        frame.grid(column=0, row=0, sticky="nsew", columnspan=5, pady=(10, 0))

        # Text label and design
        lbl_aud_report = ttk.Label(frame, text="Insert audit report ui here?", style="BlackSmall.TLabel")
        lbl_aud_report.grid(column=0, row=1, columnspan=1, sticky="", padx=5, pady=10)  # text padding

        homepage_btn = ttk.Button(
            frame,
            text="Go to Homepage",
            command=lambda: self.controller.show_frame("HomepageStart")
        )
        homepage_btn.grid(column=1, row=2, columnspan=1, sticky="es", pady=(10, 20))  # positioning

        # note to developers:
        # this is another template for whoever is working on the audit report gui
        # if you want to your next/previous page button to work:
        # Add to the top of the degreeApp.py file: from insertYourFileNameHere import insertYourClassNameHere
        # In the degreeApp.py file, add your file's class name to the () in the For Loop
        # In the button's command section, make sure the class name is enclosed in ""


