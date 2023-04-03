import tkinter as tk
from tkinter import *
from tkinter import ttk
from audit_report import AuditReport


class AuditReportPage(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller

        # Handles gui for audit report page
        style = ttk.Style(self)
        style.configure("aud_report_gui.TFrame", background="white")
        style.configure("BlackSmall.TLabel", font=("Roboto", 14), foreground="#107896", background="white")

        # Handles frame expansion when application window is expanded
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Frame background design
        frame = ttk.Frame(self, style="aud_report_gui.TFrame")
        frame["padding"] = (5, 0, 5, 0)  # adds padding for spacing aesthetic

        # Handles frame's page space distribution
        for row_index in range(6):
            frame.grid_rowconfigure(row_index, weight=1)
        for col_index in range(5):
            frame.grid_columnconfigure(col_index, weight=1)
        frame.grid(column=0, row=0, sticky="nsew", columnspan=5)

        # "Audit Report" title

        # name:, plan: Master, id:, major:, track: (based on degree plan)

        # Displays core, elective, and overall gpa

        # Displays the core (in degree plan order) and elective courses (in course number order) rows

        # Asks user if the student will be taking extra electives

        # Asks user if student is taking additional graduate courses and how many

        # User asked to select disposition of all uncompleted pre-reqs
        # list of pre-req here
        # (completed/waived/not required by plan or elective/other) options with each one
        # ...they want to assign to that class for the audit report.
        # Completed: This must be followed by semester of completion (this info would appear on transcript)
        # Waived: should have a field where the user can enter either a semester or a short comment
        # Not required by plan or electives:
        # Other: have a field where the user can enter either a semester or short comment
        # it should be none if there's no uncompleted pre-reqs (check if user selected none/no options)

        # Displays outstanding core, elective, and overall gpa requirements

        # Saves/print/generate audit report options

        # Text label and design
        lbl_aud_report = ttk.Label(frame, text="Insert audit report ui here?", style="BlackSmall.TLabel")
        lbl_aud_report.grid(column=0, row=1, columnspan=1, sticky="n", pady=10)  # text padding

        # Go to homepage button and design
        homepage_btn = ttk.Button(
            frame,
            text="Go to Homepage",
            command=lambda: self.controller.show_frame("HomepageStart")
        )
        homepage_btn.grid(column=1, row=2, columnspan=1, sticky="es", pady=(10, 20))  # positioning

        # page navigation button to work:
        # Add to the top of the degree_app.py file: from insertYourFileNameHere import insertYourClassNameHere
        # In the degree_app.py file, add your file's class name to the () in the For Loop
        # In the button's command section, make sure the class name is enclosed in ""
