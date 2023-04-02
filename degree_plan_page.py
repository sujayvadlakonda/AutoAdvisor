import tkinter as tk
from tkinter import *
from tkinter import ttk


class DegreePlanPage(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller  # allows for switching between application pages

        # Handles the gui of the Degree Plan page
        style = ttk.Style(self)
        style.configure("BlckBorder.TFrame", background="white")
        style.configure("BlSmall.TLabel", font=("Roboto", 14), foreground="#107896", background="white")

        # Handles frame expansion when application window is expanded
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Frame outline and design
        frame = ttk.Frame(self, style="BlckBorder.TFrame")

        # Handles weight distribution of the frame page
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        frame.grid_columnconfigure(3, weight=1)
        frame.grid(column=0, row=0, sticky="nsew", columnspan=5, pady=(10, 0))  # positioning

        # Previous Page button and design
        prev_btn = ttk.Button(
            frame,
            text="<< Previous",
            command=lambda: self.controller.show_frame("UploadFilePage")
        )
        prev_btn.grid(column=0, row=1, columnspan=1, sticky="sw", pady=(10, 20))  # button padding

        # Text label and design
        lbl_report = ttk.Label(frame, text="Insert degree plan ui here?:", style="BlSmall.TLabel")
        lbl_report.grid(column=1, row=0, columnspan=1, sticky="n", padx=5, pady=10)  # text padding

        # text label and design
        lbl_generate_report = ttk.Label(frame, text="Text label example:", style="BlSmall.TLabel")
        lbl_generate_report.grid(column=1, row=1, columnspan=1, padx=5, pady=10)  # text padding

        # Button to direct user to audit_report_page.py and design
        next_btn = ttk.Button(
            frame,
            text="Continue to Audit Report",
            command=lambda: controller.show_frame("AuditReportPage")
        )
        next_btn.grid(column=2, row=1, columnspan=1, pady=(10, 20))  # button padding

        # Button to direct user back to homepage
        homepage_btn = ttk.Button(
            frame,
            text="Go to Homepage",
            command=lambda: self.controller.show_frame("HomepageStart")
        )
        homepage_btn.grid(column=3, row=1, columnspan=1, pady=(10, 20))  # positioning

    # note to developers:
    # This file is just to get, whoever is working on the Degree Plan GUI, started on the gui
    # modify it as much as you want to, just make sure there's a way for the user to get to the audit report page
    # and a way for the audit_report_page.py to know which track/degree plan is chosen
    # also, in leo's design document word doc, the "degree planning report" is not the same thing as the audit report
    # if you want to your next/previous page button to work:
        # Add to the top of the degree_app.py file: from insertYourFileNameHere import insertYourClassNameHere
        # In the degree_app.py file, add your file's class name to the () in the For Loop
        # In the button's command section, make sure the class name is enclosed in ""
