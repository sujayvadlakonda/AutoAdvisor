import tkinter as tk
from tkinter import *
from tkinter import ttk
from degreeApp import DegreeApp


class Homepage(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.pack(fill=BOTH, expand=True)  # assigns ttk.Frame to root application window

        self.style = ttk.Style(self)  # keep here or in homepage_gui function

        # Handles the gui and function of the application homepage
        self.style.configure("BlBord.TFrame", borderwidth=5, background="white", relief=SOLID, height=60, width=70)
        self.style.configure("BW.TLabel", font=("Segoe Print", 30), foreground="#1496BB", background="white")
        self.style.configure("StartBig.TButton", font=("Segoe UI", 16), foreground="#ffffff", background="#086623")

        # Frame outline design
        frame = ttk.Frame(self, style="BlBord.TFrame")
        frame["padding"] = (5, 0, 5, 0)  # adjusts inner padding to fit text
        frame.pack(fill=BOTH, expand=False, pady=90)  # frame padding

        # Homepage title label and design
        lbl_upload = ttk.Label(frame, text="Degree Plan and Audit Tool", style="BW.TLabel")
        lbl_upload.pack(fill=NONE, expand=False, padx=30, pady=30)  # text padding

        # Homepage Start button and design
        #start_btn = ttk.Button(
        #    frame,
        #    text="+ Start",
        #    style="StartBig.TButton",
        #    command=self.next_page
        #)
        #start_btn.pack(side=TOP, pady=20)  # button padding

    def next_page(self):
        print("Modify this later")

        #  Segoe UI, bookman old style, bradley hand ITC, ink free, segoe print, candara light, century gothic
        #  003300, 003333, 006600, 006633, 086623 (green),
        #  107896, 1287A8, 43ABC9, #4582ec, 1496BB (blue),
        #  #593196, 7442C8, 800080, 575068 (purple)
