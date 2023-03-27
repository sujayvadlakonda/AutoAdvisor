import tkinter as tk
from tkinter import ttk
from tkinter import *
from uploadFile import UploadFile
from homepage import Homepage
from degreePlan import DegreePlan


class DegreeApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        window_name = "Degree Plan and Audit Tool"
        window_size = "760x550+270+25"
        window_color = "white"
        self.frames = {}  # initializes application page to array

        # Sets up the application window
        self.config(background=window_color)  # Window background color
        self.geometry(window_size)  # Window size
        self.title(window_name)  # Window name
        icon = tk.PhotoImage(file="./images/project_icon.png")
        self.iconphoto(FALSE, icon)  # window icon logo

        # Sets up application container and placement
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Handles switching between application pages
        for class_Name in (Homepage, UploadFile, DegreePlan):
            frame = class_Name(container, self)  # Handles Frame's parameter where self=controller
            self.frames[class_Name] = frame  # initializes each page of application
            frame.grid(row=0, column=0, sticky="nsew")  # keeps pages bundled in the same location

        self.show_frame(Homepage)  # Displays application homepage

    # Displays page the user navigated to
    def show_frame(self, pg_count):
        frame = self.frames[pg_count]
        frame.tkraise()
