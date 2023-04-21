import tkinter as tk
from tkinter import ttk
from tkinter import *
from upload_file_page import UploadFilePage
from homepage import HomepageStart
from degree_plan_page import DegreePlanPage
from degree_plan_report_page import DegreePlanReportPage
from audit_report_page import AuditReportPage


class DegreeApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        window_name = "Degree Plan and Audit Tool"
        window_size = "950x700+270+25"
        window_color = "white"
        self.frames = {}  # initializes application pages to dictionary

        # Sets up the application window
        self.config(background=window_color)  # Window background color
        self.geometry(window_size)  # Window size
        self.title(window_name)  # Window name
        icon = tk.PhotoImage(file="./images/project_icon.png")
        self.iconphoto(FALSE, icon)  # window icon logo

        # Sets up application frame container and placement
        container = ttk.Frame(self)
        container.pack(expand=TRUE, fill=BOTH, side=TOP)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        # Handles switching between application pages using Class Names
        for class_Name in (HomepageStart, UploadFilePage, DegreePlanPage, DegreePlanReportPage, AuditReportPage):
            page_name = class_Name.__name__
            frame = class_Name(container, self)  # creates instance of each class where self=controller
            frame.grid(column=0, row=0, sticky="nsew")  # keeps pages bundled when moving the Window
            self.frames[page_name] = frame  # initializes classes

        self.show_frame("HomepageStart")  # Displays application homepage

    # Displays page the user navigated to
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
