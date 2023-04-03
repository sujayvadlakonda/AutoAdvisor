import tkinter as tk
from tkinter import *
from tkinter import ttk


class DegreePlanReportPage(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller  # allows for switching between application pages

        # Handles Editable Degree Plan Report page's widget style options
        style = ttk.Style(self)
        style.configure("reportScreen.TFrame", background="white")
        style.configure("BlSmall.TLabel", font=("Roboto", 14), foreground="#107896", background="white")

        # Handles frame expansion when application window is expanded
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Frame outline and design
        frame = ttk.Frame(self, style="reportScreen.TFrame")

        # Handles weight distribution of the frame page's rows and columns
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        frame.grid_columnconfigure(3, weight=1)
        frame.grid(column=0, row=0, sticky="nsew", columnspan=5)  # frame positioning

        # Text label and design
        lbl_dp_report = ttk.Label(frame, text="Teammate's add way for user to edit degree plan here?:", style="BlSmall.TLabel")
        lbl_dp_report.grid(column=1, row=0, columnspan=3, sticky="n", padx=5, pady=10)  # text positioning

        # insert here a way for user to edit degree plan (move/add/change/delete courses and pre-requisite's)?

        # Insert here a way for user to generate & save a student object (that has the new changes) via clicking a button?

        # Insert here a way for user to generate, save and/or print degree plan (pdf?) they've finished changing?

        # Previous Page button and design
        prev_btn = ttk.Button(
            frame,
            text="<< Previous",
            command=lambda: self.controller.show_frame("DegreePlanPage")
        )
        prev_btn.grid(column=0, row=1, columnspan=1, sticky="sw", padx=(5, 0), pady=(10, 20))  # button positioning

        # Button to direct user to audit_report_page.py and design
        next_btn = ttk.Button(
            frame,
            text="Continue to Audit Report",
            command=lambda: controller.show_frame("AuditReportPage")
        )
        next_btn.grid(column=1, row=1, columnspan=1, pady=(10, 20))  # button positioning

        # Button to direct user back to homepage
        homepage_btn = ttk.Button(
            frame,
            text="Go to Homepage",
            command=lambda: self.controller.show_frame("HomepageStart")
        )
        homepage_btn.grid(column=2, row=1, columnspan=1, pady=(10, 20))  # positioning

        # note to the developer in charge of the degree plan gui:
        # This file is just to get, whoever is working on the Degree Plan GUI, a head start on the gui.
        # there's still the rest of the gui etc. that you'll need to figure out and add to this
        # modify it as much as you want to, just make sure to:
        # include a way for the user to get to the audit report page...
        # ...and a way for audit_report_page.py to know what prerequisite courses the audit report needs to deal with
        # the "degree planning report" in the design document is not the same thing as an audit report
