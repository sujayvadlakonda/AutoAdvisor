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
        self.style.configure("BlBord.TFrame", borderwidth=5, background="white", relief=SOLID, height=60, width=70)
        self.style.configure("BW.TLabel", font=("Segoe Print", 30), foreground="#0032A0", background="white")
        self.style.configure("StartBig.TButton", font=("Segoe UI", 16), foreground="black", background="#553980")

        # Frame outline design
        frame = ttk.Frame(self, style="BlBord.TFrame")
        frame["padding"] = (5, 0, 5, 0)  # adjusts inner padding to fit text
        frame.pack(fill=BOTH, expand=False, pady=90)  # frame padding

        # Homepage title label and design
        lbl_upload = ttk.Label(frame, text="Degree Plan and Audit Tool", style="BW.TLabel")
        lbl_upload.pack(side=TOP, padx=30, pady=30)  # text padding

        # Homepage Start button and design
        start_btn = ttk.Button(
            frame,
            text="+ Start",
            style="StartBig.TButton",
            command=lambda: controller.show_frame(UploadFile)
        )
        start_btn.pack(side=TOP, pady=20)  # button padding
