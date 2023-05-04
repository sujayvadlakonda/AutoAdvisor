import tkinter as tk
from tkinter import *
from tkinter import ttk
from plan_printer import *
from tkinter.messagebox import showinfo


class DegreePlanPage(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller  # allows for switching between application pages
        self.ft_selected = tk.StringVar()
        self.thesis_selected = tk.StringVar()
        self.expect_grad = tk.StringVar()
        # self.track_selected = ""
        self.track_selected = tk.StringVar()
        self.advisor_name = tk.StringVar()
        self.date_submitted = tk.StringVar()
        self.path_to_pdf = tk.StringVar()

        # When update new track.
        # Make sure update both from here and degree_requirement.py file
        dict_track_options = {'Data Sciences':'data_science',
                                'Systems':'systems',
                                'Interactive Computing':'interactive_computing',
                                'Cyber Security':'cyber_security',
                                'Intelligent Systems':'intelligent_systems',
                                'Networks and Telecommunications':'networks_telecommunication',
                                'Traditional Computer Science':'traditional',
                                'Software Engineering':'software_engineering'}

        # Handles Degree Plan page style options
        style = ttk.Style(self)
        style.configure("dp_gui.TFrame", background="black", relief="flat")
        style.configure("section.TFrame", background="orange", relief="raised")

        style.configure("big_heading.TLabel", font=("Segoe print", 30, "bold"), foreground="black", background="orange")
        style.configure("medium_heading.TLabel", font=("Verdana", 25), foreground="black", background="orange")
        style.configure("bold_heading.TLabel", font=("Segoe print", 25, "bold"), foreground="black",
                        background="orange")

        style.configure("normal_text.TLabel", font=("Bookman Old Style", 14), foreground="black", background="orange")
        style.configure("filling_text.TLabel", font=("Bookman Old Style", 14), foreground="black", background="white",
                        relief="sunken")
        style.configure("course_section.TLabel", font=("Bookman Old Style", 14), foreground="orange",
                        background="black")

        style.configure("TRadiobutton", font=("Bookman Old Style", 14), foreground="black", background="orange",
                        relief="flat")

        # Handles frame expansion when application window is expanded
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Create Degree Plan Frame
        frame = ttk.Frame(self, style="dp_gui.TFrame")
        frame["padding"] = 10
        frame.columnconfigure(0, weight=1)
        section = 11
        for r in range(section):
            frame.rowconfigure(r, weight=1)
        frame.pack(expand=TRUE, fill=BOTH, side=TOP)

        # Creating frame sections
        # 0. Gui Title Frame
        fr_titleGui = ttk.Frame(frame, style="section.TFrame")
        fr_titleGui.columnconfigure(0, weight=1)
        fr_titleGui.rowconfigure(0, weight=1)
        fr_titleGui.grid(column=0, row=0, sticky="nsew", pady=5)

        lbl_gui = ttk.Label(fr_titleGui, text="DEGREE PLAN EDITOR", style="big_heading.TLabel")
        lbl_gui.grid(column=0, row=0, pady=5)  # text positioning

        # 1. Title Frame
        c1 = 0
        r1 = 4
        fr_title = ttk.Frame(frame, style="section.TFrame")
        fr_title.columnconfigure(0, weight=1)
        for r in range(r1):
            fr_title.rowconfigure(r, weight=1)
        fr_title.grid(column=0, row=1, sticky="nsew", pady=5)

        # Labeling
        lbl_title = ttk.Label(fr_title, text="DEGREE PLAN", style="medium_heading.TLabel")
        lbl_title.grid(column=0, row=0, pady=(10, 5))
        lbl_title = ttk.Label(fr_title, text="UNIVERSITY OF TEXAS AT DALLAS", style="medium_heading.TLabel")
        lbl_title.grid(column=0, row=1)
        lbl_title = ttk.Label(fr_title, text="MASTER OF COMPUTER SCIENCE", style="medium_heading.TLabel")
        lbl_title.grid(column=0, row=2)

        # Get and Display Student's Major
        self.lbl_major = ttk.Label(fr_title, text='', style="bold_heading.TLabel")
        self.lbl_major.grid(column=0, row=4, pady=(0, 10))

        # 2. Student Frame
        c2 = 6
        r2 = 3
        fr_student = ttk.Frame(frame, style="section.TFrame")
        for c in range(c2):
            fr_student.columnconfigure(c, weight=1)
        for r in range(r2):
            fr_student.rowconfigure(r, weight=1)
        fr_student.grid(column=0, row=2, sticky="nsew", pady=5)

        # Labeling
        # Student Name
        lbl_student = ttk.Label(fr_student, text="Name of Student:", style="normal_text.TLabel")
        lbl_student.grid(column=0, row=0, sticky='w', padx=5, pady=(10, 5))

        self.lbl_student_name = ttk.Label(fr_student, text='', style="filling_text.TLabel")
        self.lbl_student_name.grid(column=1, row=0, sticky='w', padx=5, pady=5)

        # Student ID
        lbl_student = ttk.Label(fr_student, text="Student ID Number:", style="normal_text.TLabel")
        lbl_student.grid(column=0, row=1, sticky='w', padx=5, pady=5)

        self.lbl_student_id = ttk.Label(fr_student, text='', style="filling_text.TLabel")
        self.lbl_student_id.grid(column=1, row=1, sticky='w', padx=5, pady=5)

        # Semester Admitted
        lbl_student = ttk.Label(fr_student, text="Semester Admitted \n to Program:", style="normal_text.TLabel")
        lbl_student.grid(column=0, row=2, sticky='w', padx=5, pady=(5, 10))

        self.lbl_student_admit = ttk.Label(fr_student, text='', style="filling_text.TLabel")
        self.lbl_student_admit.grid(column=1, row=2, sticky='w', padx=5, pady=5)

        #   FT, Thesis, Anticipated
        options = (('Yes', "Y"),
                   ('No', "N"))

        # Fast Track
        lbl_student = ttk.Label(fr_student, text="FT:", style="normal_text.TLabel")
        lbl_student.grid(column=2, row=0, sticky='w', padx=5, pady=5)
        c_index = 3
        r_index = 0
        for opt in options:
            ft_rdb = ttk.Radiobutton(
                fr_student,
                text=opt[0],
                value=opt[1],
                variable=self.ft_selected,
                style="TRadiobutton"
            )
            ft_rdb.grid(column=c_index, row=r_index, sticky='w', padx=(10, 0))
            c_index += 1

        # Thesis
        lbl_student = ttk.Label(fr_student, text="Thesis:", style="normal_text.TLabel")
        lbl_student.grid(column=2, row=1, sticky='w', padx=5, pady=5)
        c_index = 3
        r_index = 1
        for opt in options:
            thesis_rdb = ttk.Radiobutton(
                fr_student,
                text=opt[0],
                value=opt[1],
                variable=self.thesis_selected,
                style="TRadiobutton"
            )
            thesis_rdb.grid(column=c_index, row=r_index, sticky='w', padx=(10, 0))
            c_index += 1

        # Anticipated Graduation
        lbl_student = ttk.Label(fr_student, text="Anticipated \n Graduation", style="normal_text.TLabel")
        lbl_student.grid(column=2, row=2, sticky='w', padx=5, pady=5)

        entry_student = ttk.Entry(fr_student, textvariable=self.expect_grad, font=("Bookman Old Style", 14), foreground="black")
        entry_student.grid(column=3, row=2, sticky='w', columnspan=2)


        # Track Selection
        lbl_student = ttk.Label(fr_student, text="Track Selections", style="normal_text.TLabel")
        lbl_student.grid(column=5, row=0, sticky='w', padx=5, pady=5)

        # Track Options List
        current_dropbox_value = tk.StringVar()
        cbb_student_track = ttk.Combobox(fr_student,
                                         textvariable=current_dropbox_value,
                                         value=list(dict_track_options.keys()),
                                         state='readonly',
                                         font=("Bookman Old Style", 14), foreground="black")
        cbb_student_track.grid(column=5, row=1, sticky='w', padx=5, pady=5)

        # Bind the selected value changes
        def get_track(event):
            self.track_selected = current_dropbox_value.get()
            arp = self.controller.get_page("AuditReportPage")
            arp.student_track = self.track_selected

        cbb_student_track.bind('<<ComboboxSelected>>', get_track)

        # 3. Linkup Frame
        c_link = 2
        r_link = 1
        fr_link = ttk.Frame(frame, style="section.TFrame")
        for c in range(c_link):
            fr_link.columnconfigure(c, weight=1)
        for r in range(r_link):
            fr_link.rowconfigure(r, weight=1)
        fr_link.grid(column=0, row=4, sticky="nsew", pady=5)

        # Previous Page Button
        prev_btn = ttk.Button(
            fr_link,
            text="<< Previous",
            command=lambda: self.controller.show_frame("UploadFilePage")
        )
        prev_btn.grid(column=0, row=0, sticky='w', padx=(10, 5), pady=10)  # button positioning

        # Go to Homepage Button
        homepage_btn = ttk.Button(
            fr_link,
            text="Go to Homepage",
            command=lambda: self.controller.show_frame("HomepageStart")
        )
        homepage_btn.grid(column=0, row=0, padx=5, pady=10)  # button positioning

        def launch_pdf():
            path = self.path_to_pdf

            if self.ft_selected.get() == "Y":
                ft = True
            else:
                ft = False

            if self.thesis_selected.get() == "Y":
                thesis = True
            else:
                thesis = False

            grad = self.expect_grad.get()
            advisor = self.advisor_name.get()
            date = self.date_submitted.get()
            track = dict_track_options[self.track_selected]

            gui_entry = [ft, thesis, grad, track, advisor, date]
            plan_printer(path, gui_entry)

        # Launch PDF Button
        launch_pdf_btn = ttk.Button(
            fr_link,
            text="Launch PDF Editor",
            command=launch_pdf
        )
        launch_pdf_btn.grid(column=1, row=0, padx=5, pady=10)  # button positioning

        # Next Button
        next_btn = ttk.Button(
            fr_link,
            text="Next >>",
            command=lambda: controller.show_frame("AuditReportPage")
        )
        next_btn.grid(column=1, row=0, sticky="e", padx=(0, 10), pady=10)  # button padding

