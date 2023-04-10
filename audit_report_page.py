import tkinter as tk
import os
from tkinter import *
from tkinter import ttk, filedialog
from docx import Document
# from audit_report import AuditReport


class AuditReportPage(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller

        # Handles gui for audit report page
        style = ttk.Style(self)
        style.configure("aud_report_gui.TFrame", background="white")
        style.configure("BlWht.TLabel", font=("Segoe UI", 20), foreground="black", background="white")
        style.configure("BlackSmall.TLabel", font=("Arial", 14), foreground="black", background="orange")
        style.configure("Black_txt.TLabel", font=("Calibri", 12), foreground="black", background="green")
        style.configure("input.TRadiobutton", background="pink")

        # Handles frame expansion when application window is expanded
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Frame background design
        frame = ttk.Frame(self, style="aud_report_gui.TFrame")

        # Background Frame's page space distribution starting from row 0, column 0
        for row_index in range(49):
            frame.grid_rowconfigure(row_index, weight=1)
        for col_index in range(15):
            frame.grid_columnconfigure(col_index, weight=1)
        frame.grid(column=0, row=0, sticky="nsew", columnspan=16)

        # Canvas to hold scrollbar
        canvas = tk.Canvas(frame, bg="white", bd=0, highlightthickness=0)
        canvas.grid(column=0, row=0, sticky="nsew", rowspan=50)  # positioning

        # Page Scrollbar and design
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=15, rowspan=50, sticky="ns")  # positioning

        # Frame to hold contents to scroll
        scrollable_frame = ttk.Frame(canvas, style="aud_report_gui.TFrame")
        scrollable_frame["padding"] = (5, 0, 5, 0)  # adds padding for spacing aesthetic

        # Scrollable frame page space distribution
        for row_index in range(49):
            scrollable_frame.grid_rowconfigure(row_index, weight=1)
        for col_index in range(15):
            scrollable_frame.grid_columnconfigure(col_index, weight=1)

        # Canvas Design and expansion
        canvas_win = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")  # positioning
        canvas.bind('<Configure>', lambda e: canvas.itemconfig(canvas_win, width=e.width, height=e.height))
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"), width=e.width))
        canvas.configure(yscrollcommand=scrollbar.set)  # sets scrollbar

        # Audit Report page title and design
        lbl_aud_report = ttk.Label(scrollable_frame, text="Audit Report", style="BlWht.TLabel")
        lbl_aud_report.grid(column=1, row=0, columnspan=2, sticky="nw", pady=(5, 10))  # text positioning

        document = Document()  # sets up Word doc object to generate audit report

        # Displays "Audit Report" title sent in file (centered and bolded)

        # Displays student information in file
        # Student Name: (r1 left side, title bold)
        # ID: (r1 right side, title bold)
        # Plan: Master (r2 Left Side, title bold)
        # Major: (r2 right side, title bold)
        # Track: (r3 right side, based on degree plan, title bold)

        # Displays core, elective, and overall gpa label on screen
        lbl_core_gpa = ttk.Label(scrollable_frame, text="Core GPA: ", style="BlackSmall.TLabel")
        lbl_core_gpa.grid(column=0, row=6, columnspan=1, sticky="w", pady=(10, 0))  # text positioning
        lbl_elective_gpa = ttk.Label(scrollable_frame, text="Elective GPA: ", style="BlackSmall.TLabel")
        lbl_elective_gpa.grid(column=0, row=7, columnspan=1, sticky="w")  # text positioning
        lbl_overall_gpa = ttk.Label(scrollable_frame, text="Overall GPA: ", style="BlackSmall.TLabel")
        lbl_overall_gpa.grid(column=0, row=8, columnspan=1, sticky="w", pady=(0, 10))  # text positioning

        # Displays core, elective, and overall gpa on screen
        # self.core_gpa = ""
        # self.elective_gpa = ""
        # self.overall_gpa = ""
        # lbl_core_gpa_display = ttk.Label(scrollable_frame, text=self.core_gpa, style="Black_txt.TLabel")
        # lbl_core_gpa_display.grid(column=1, row=6, columnspan=1, sticky="w", pady=(10, 0))  # text positioning
        # lbl_elective_gpa_display = ttk.Label(scrollable_frame, text=self.elective_gpa, style="Black_txt.TLabel")
        # lbl_elective_gpa_display.grid(column=1, row=7, columnspan=1, sticky="w")  # text positioning
        # lbl_overall_gpa_display = ttk.Label(scrollable_frame, text=self.overall_gpa, style="Black_txt.TLabel")
        # lbl_overall_gpa_display.grid(column=1, row=8, columnspan=1, sticky="w", pady=(0, 10))  # text positioning

        # Displays core, elective, and overall gpa in file
        # Displays "Core GPA" row in file (r1, title bold)
        # Displays "Elective GPA" row in file (r2, title bold)
        # Displays "Overall GPA" row in fil (r3, title bold)

        # Displays "Core Courses" row in file (in degree plan order, title bold)
        # Displays "Elective Courses" row in file (in course number order, title bold)

        # Prompts user to answer questions label and design
        lbl_xtra_elect = ttk.Label(scrollable_frame, text="Answer the Following Questions:", style="BlackSmall.TLabel")
        lbl_xtra_elect.grid(column=0, row=11, columnspan=2, sticky="w", pady=(10, 10))  # positioning

        # Asks user if student will be taking extra electives (used for elective gpa calculations)
        select_elective = tk.StringVar()
        confirm_options = (("Yes", "Correct"), ("No", "Incorrect"))
        lbl_xtra_elect = ttk.Label(scrollable_frame, text="Student taking extra electives:", style="BlackSmall.TLabel")
        lbl_xtra_elect.grid(column=0, row=12, columnspan=2, sticky="w", pady=(10, 10))  # positioning

        # Taking Extra Electives question options
        index = 2
        for option in confirm_options:
            lbl_confirm_elective = ttk.Radiobutton(
                scrollable_frame,
                text=option[0],
                value=option[1],
                variable=select_elective,
                style="input.TRadiobutton"
            )
            lbl_confirm_elective.grid(column=index, row=12, columnspan=1, sticky="w", pady=(10, 10))  # positioning
            index = index+1
        xtra_elective_result = select_elective.get()  # holds user selection of question

        # Asks user if student is taking additional graduate courses and how many (used for gpa calculations)
        select_addi_class = tk.StringVar()
        grad_course_question = "Student taking additional graduate courses:"
        lbl_grad_class = ttk.Label(scrollable_frame, text=grad_course_question, style="BlackSmall.TLabel")
        lbl_grad_class.grid(column=0, row=13, columnspan=3, sticky="w", pady=(10, 10))  # text positioning

        # Taking additional graduate courses question options
        col = 3
        for option in confirm_options:
            lbl_class_quantity = ttk.Radiobutton(
                scrollable_frame,
                text=option[0],
                value=option[1],
                variable=select_addi_class,
                style="input.TRadiobutton"
            )
            lbl_class_quantity.grid(column=col, row=13, columnspan=1, sticky="w", pady=(10, 10))  # positioning
            col = col+1
        addi_class_result = str(select_addi_class.get())  # holds user selection variable of question

        # Asks user how many additional graduate courses the student is taking
        class_quantity = tk.StringVar()
        class_amount_question = "Enter additional graduate course quantity:"
        if addi_class_result == "Correct":
            lbl_quan_class = ttk.Label(scrollable_frame, text=class_amount_question, style="BlackSmall.TLabel")
            lbl_quan_class.grid(column=0, row=14, columnspan=3, sticky="w", pady=(10, 10))  # text positioning
        # Entry box to enter how many additional graduate courses the student is taking

        # Displays "Leveling Courses and Pre-requisites from Admission Letter:" title in file (bold)

        # User asked to select disposition of all uncompleted pre-reqs from degree plan
        # ((completed/waived/not required by plan or elective/other) options with each one)
        # Completed: This must be followed by semester of completion (this info would appear on transcript)
        # Waived: should have a field where the user can enter either a semester or a short comment
        # Not required by plan or electives:
        # Other: have a field where the user can enter either a semester or short comment
        # it should be "None" if there's no uncompleted pre-reqs (check if user selected none/no options)
        # display course abbrev and #: disposition
        pre_req_prompt = "Select Student's Prerequisite Course(s) Disposition:"
        lbl_pre_req = ttk.Label(scrollable_frame, text=pre_req_prompt, style="BlackSmall.TLabel")
        lbl_pre_req.grid(column=0, row=15, columnspan=4, sticky="ew", pady=(10, 0))  # text positioning
        # add text variable for each course (7 rows, adjusted with if statement)

        # Displays "Outstanding Requirements:" title to file and screen
        lbl_gpa_req = ttk.Label(scrollable_frame, text="Outstanding Requirements:", style="BlackSmall.TLabel")
        lbl_gpa_req.grid(column=0, row=42, columnspan=2, sticky="w", pady=(10, 5))  # text positioning

        # Displays outstanding core, elective, and overall gpa requirements on screen and file
        # If GPA needed in remaining course(s) is >= 2.00:
        # then, if one course remaining display: The student needs >= C+, B-, etc. in CS xxxx
        # or if multiple courses remaining display: The student needs a GPA >= x.xx in: CS xxxx, CS xxxx, etc.
        # If GPA needed in remaining course(s) is < 2.00: Display: The student must pass CS xxxx, CS xxxx, etc.
        # or if the course completed then e.g. Core Complete.

        # Saves printable audit report in File Explorer
        audit_report_btn = ttk.Button(
            scrollable_frame,
            text="Save Audit Report",
            command=lambda: self.save_file()
        )
        audit_report_btn.grid(column=13, row=49, columnspan=1, sticky="sw", padx=(0, 5), pady=(20, 20))  # positioning

        # Previous Page button and design
        prev_btn = ttk.Button(
            scrollable_frame,
            text="<< Previous",
            command=lambda: self.controller.show_frame("DegreePlanReportPage")
        )
        prev_btn.grid(column=0, row=49, columnspan=1, sticky="sw", padx=(5, 0), pady=(20, 20))  # button positioning

        # Go to homepage button and design
        homepage_btn = ttk.Button(
            scrollable_frame,
            text="Go to Homepage",
            command=lambda: self.controller.show_frame("HomepageStart")
        )
        homepage_btn.grid(column=14, row=49, columnspan=1, sticky="se", pady=(20, 20))  # positioning

    # Handles saving the audit report file in file explorer
    def save_file(self):
        word_doc = "Microsoft Word Document"
        file_types = [("All Files", "*.*"), (word_doc, "*.docx*")]

        # currently being revamped
        # if os.name == 'posix':
            # audit_filename = filedialog.asksaveasfile(initialdir="/", title="Open")
        # else:
            # audit_filename = filedialog.asksaveasfilename(initialdir="\\", title="Open", filetypes=file_types)
