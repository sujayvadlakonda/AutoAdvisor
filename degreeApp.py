import tkinter as tk
from tkinter import *
from tkinter import ttk

# Handles the application window
class DegreeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        window_name = "Degree Plan and Audit Tool"
        window_size = "700x550+270+25"
        window_color = "white"

        self.config(background=window_color)  # Window background color
        self.geometry(window_size)  # Window size
        self.title(window_name)  # Window name
        icon = tk.PhotoImage(file="./images/project_icon.png")
        self.iconphoto(FALSE, icon)  # window icon logo
