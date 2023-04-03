import tkinter as tk
from tkinter import *
from tkinter import ttk


class DegreePlanPage(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller  # allows for switching between application pages

        # Handles Degree Plan page style options
        style = ttk.Style(self)
        style.configure("BlckBorder.TFrame", background="white")
        style.configure("BlSmall.TLabel", font=("Roboto", 14), foreground="#107896", background="white")

        # Handles frame expansion when application window is expanded
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Frame outline and design
        frame = ttk.Frame(self, style="BlckBorder.TFrame")
        frame["padding"] = (5, 0, 5, 0)  # adjusts inner padding for spacing

        # Handles weight distribution of the frame page (you can also just use a For Loop)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        frame.grid_columnconfigure(3, weight=1)
        frame.grid(column=0, row=0, sticky="nsew", columnspan=5)  # positioning

        # Text label and design
        lbl_dp = ttk.Label(frame, text="Teammate's degree plan/student object related gui goes here?:", style="BlSmall.TLabel")
        lbl_dp.grid(column=1, row=0, columnspan=3, sticky="n", pady=10)  # text positioning

        # Choose student's degree plan track text label and design
        # lbl_dp_track = ttk.Label(frame, text="Choose student's chosen track/Degree Plan:", style="BlSmall.TLabel")
        # lbl_dp_track.grid(column=1, row=1, columnspan=1, padx=5, pady=10)  # text positioning

        # Insert here a Degree Plan Track options list, where the user can add/select/change/remove tracks?

        # Insert here a list of prerequisite courses, where the user can change/delete/add new/add to degree plan?

        # save what track option was selected in a way that the audit report can access it

        # Insert here a way for user to select if the student is doing Fast Track, and save value to student object?

        # Insert here a way for user to select if the student is doing Thesis, and save value to student object?

        # Insert here way for user to generate & save student object with a click of a button?

        # Previous Page button and design
        prev_btn = ttk.Button(
            frame,
            text="<< Previous",
            command=lambda: self.controller.show_frame("UploadFilePage")
        )
        prev_btn.grid(column=0, row=1, columnspan=1, sticky="sw", padx=(5, 0), pady=(10, 20))  # button positioning

        # Button to direct user to degree_plan_report_page.py in order for user to edit degree plan
        next_btn = ttk.Button(
            frame,
            text="Next >>",
            command=lambda: controller.show_frame("DegreePlanReportPage")
        )
        next_btn.grid(column=4, row=1, columnspan=1, sticky="es", pady=(10, 20))  # button padding

    # note to the developer in charge of the degree plan gui:
    # This file is just to get, whoever is working on the Degree Plan GUI, a head start on the gui.
    # there's still the rest of the gui, student object stuff, etc. that you'll need to figure out and add to this
    # modify it as much as you want to, just make sure to:
    # include a way for audit_report_page.py to know what degree plan track and prerequisite courses are chosen
