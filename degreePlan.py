import tkinter as tk
from tkinter import *
from tkinter import ttk


class DegreePlan(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller

        self.style = ttk.Style(self)
        self.style.configure("BlckBorder.TFrame", borderwidth=5, background="white", relief=SOLID, height=60, width=70)

        # Frame outline design
        frame = ttk.Frame(self, style="BlckBorder.TFrame")
        frame["padding"] = (5, 0, 5, 0)  # adjusts inner padding to fit text
        frame.pack(fill=BOTH, expand=False, pady=90)  # frame padding

        # Previous page button
        prev_btn = ttk.Button(
            frame,
            text="<< Previous",
            command=lambda: controller.show_frame("UploadFile")
        )
        prev_btn.pack(pady=(5, 20))  # button padding

        # Next page button and design
        #next_btn = ttk.Button(
            #frame,
            #text="Next >>",
            #command=lambda: controller.show_frame("Insert class name of next page here")
        #)
        #next_btn.pack(pady=(5, 20))  # button padding

        # note to developers if you want to your next/previous page button to work:
        # Add to the top of the degreeApp.py+current file: from insertFileNameHere import insertClassNameHere
        # In the degreeApp.py file, add your file's class name to the () in the For Loop
