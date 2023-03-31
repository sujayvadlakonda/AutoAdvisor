import tkinter as tk
from tkinter import *
from tkinter import ttk


class HomepageStart(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller  # Used to control which page is shown

        # Handles the gui of the application homepage
        style = ttk.Style(self)
        style.configure("BlckBord.TFrame", borderwidth=5, background="#97DFFC", relief=SOLID)
        style.configure("CW.TLabel", font=("Segoe print", 30), foreground="#0032A0", background="#97DFFC")
        style.configure("GrySmall.TLabel", font=("Bookman Old Style,", 14), foreground="#343a40", background="#97DFFC")

        # Frame outline design
        frame = ttk.Frame(self, style="BlckBord.TFrame")
        frame["padding"] = (5, 0, 5, 0)  # adjusts inner padding to fit text
        frame.pack(fill=BOTH, pady=(60, 0))  # frame padding

        # Homepage title label and design
        lbl_upload = ttk.Label(frame, text="Degree Plan and Audit Tool", style="CW.TLabel")
        lbl_upload.pack(side=TOP, pady=(70, 10))  # frame padding

        # subtext label and design
        lbl_upload = ttk.Label(frame, text="Press the Start Button to Begin", style="GrySmall.TLabel")
        lbl_upload.pack(side=TOP, pady=(40, 20))  # frame padding

        # Homepage Start button functionality and design
        start_btn = tk.Button(
            frame,
            text=" + Start ",
            font=("Segoe UI", 16),
            foreground="white",
            background="#553980",
            bd="5",
            width="10",
            relief="raised",
            command=lambda: self.controller.show_frame("UploadFilePage")
        )
        start_btn.pack(side=TOP, pady=(40, 90))  # frame padding
