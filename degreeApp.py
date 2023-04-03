import tkinter as tk
from tkinter import ttk
from tkinter import *
from uploadFile import UploadFilePage
from homepage import HomepageStart
from degreePlan import DegreePlanPage
from auditReport import AuditReportPage


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
        container.pack(expand=TRUE, fill=BOTH, side=TOP)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        # Handles switching between application pages using Class Names
        for class_Name in (HomepageStart, UploadFilePage, DegreePlanPage, AuditReportPage):
            pg_name = class_Name.__name__
            frame = class_Name(container, self)  # creates instance of each class where self=controller
            self.frames[pg_name] = frame  # initializes each class of application
            frame.grid(column=0, row=0, sticky="nsew")  # keeps pages bundled in the same location

        self.show_frame("HomepageStart")  # Displays application homepage

    # Displays page the user navigated to
    def show_frame(self, pg_name):
        frame = self.frames[pg_name]
        frame.tkraise()
