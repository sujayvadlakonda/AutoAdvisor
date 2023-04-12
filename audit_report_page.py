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
        self.style = ttk.Style(self)
        self.style.configure("aud_report_gui.TFrame", background="white")
        self.style.configure("BlWht.TLabel", font=("Segoe UI", 20), foreground="black", background="white")
        self.style.configure("BlackSmall.TLabel", font=("Arial", 14), foreground="black", background="orange")
        self.style.configure("Black_txt.TLabel", font=("Calibri", 12), foreground="black", background="green")
        self.style.configure("input.TRadiobutton", background="pink")
        self.style.configure("data.TEntry", background="yellow")

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
        canvas.grid(column=0, row=0, sticky="nsew", columnspan=15, rowspan=50)  # positioning

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

        # Canvas Design
        canvas_win = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")  # positioning
        canvas.bind('<Configure>', lambda e: canvas.itemconfig(canvas_win, width=e.width))
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.configure(yscrollcommand=scrollbar.set)  # sets scrollbar

        # Handles scrolling the frame based on OS when hovering over the scrollbar
        if os.name == "posix":
            scrollable_frame.bind("<Enter>", lambda e: scrollable_frame.bind_all('<MouseWheel>',  canvas.yview_scroll(int(e.delta), "units")))
            scrollable_frame.bind("<Leave>", lambda e: scrollable_frame.unbind_all('<MouseWheel>'))
        else:
            scrollable_frame.bind("<Enter>", lambda e: scrollable_frame.bind_all('<MouseWheel>', canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")))
            scrollable_frame.bind("<Leave>", lambda e: scrollable_frame.unbind_all('<MouseWheel>'))

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
        # waiting on akelanda for this section

        # Displays core, elective, and overall gpa in file
        # Displays "Core GPA" row in file (r1, title bold)
        # Displays "Elective GPA" row in file (r2, title bold)
        # Displays "Overall GPA" row in fil (r3, title bold)

        # Displays "Core Courses" row in file (in degree plan order, title bold)
        # Displays "Elective Courses" row in file (in course number order, title bold)
        # sujay's sections

        # Prompts user to answer questions label and design
        lbl_xtra_elect = ttk.Label(scrollable_frame, text="Answer the Following Questions:", style="BlackSmall.TLabel")
        lbl_xtra_elect.grid(column=0, row=11, columnspan=2, sticky="w", pady=(10, 10))  # positioning

        # Asks user if student will be taking extra electives (used for elective gpa calculations)
        lbl_xtra_elect = ttk.Label(scrollable_frame, text="Student taking extra electives:", style="BlackSmall.TLabel")
        lbl_xtra_elect.grid(column=0, row=12, columnspan=2, sticky="w", pady=(10, 10))  # positioning

        # Taking Extra Electives question selection options
        select_elective = tk.StringVar(scrollable_frame)
        elective_confirm = ttk.Radiobutton(
            scrollable_frame,
            text="Yes",
            value="Correct",
            variable=select_elective,
            style="input.TRadiobutton"
        )
        elective_confirm.grid(column=2, row=12, columnspan=1, sticky="w", pady=(10, 10))  # positioning
        elective_deny = ttk.Radiobutton(
            scrollable_frame,
            text="No",
            value="Incorrect",
            variable=select_elective,
            style="input.TRadiobutton"
        )
        elective_deny.grid(column=3, row=12, columnspan=1, sticky="w", pady=(10, 10))  # positioning
        xtra_elective_result = select_elective.get()  # holds user selection of question

        # Asks user if student is taking additional graduate courses and how many (used for gpa calculations)
        grad_course_question = "Student taking additional graduate courses:"
        lbl_grad_class = ttk.Label(scrollable_frame, text=grad_course_question, style="BlackSmall.TLabel")
        lbl_grad_class.grid(column=0, row=13, columnspan=3, sticky="w", pady=(10, 10))  # text positioning

        # Taking Additional Graduate Courses question selection options
        select_addi_class = tk.StringVar(scrollable_frame)
        addi_courses_confirm = ttk.Radiobutton(
            scrollable_frame,
            text="Yes",
            value="Correct",
            variable=select_addi_class,
            style="input.TRadiobutton"
            # add command here to add stuff to canvas
        )
        addi_courses_confirm.grid(column=3, row=13, columnspan=1, sticky="w", pady=(10, 10))  # positioning
        elective_deny = ttk.Radiobutton(
            scrollable_frame,
            text="No",
            value="Incorrect",
            variable=select_addi_class,
            style="input.TRadiobutton"
        )
        elective_deny.grid(column=4, row=13, columnspan=1, sticky="w", pady=(10, 10))  # positioning
        # addi_class = select_addi_class
        # addi_class_result = str(addi_class.get())  # holds user selection variable of question

        # Asks user how many additional graduate courses the student is taking
        class_quantity = tk.StringVar(scrollable_frame)
        class_amount_question = "If yes, enter additional graduate course quantity:"
        if select_addi_class.get() == "Correct":
            # result := select_addi_class.get()) == "Correct":
            # class_res = select_addi_class.get()
            # print(addi_class_result)
            lbl_quan_class = ttk.Label(scrollable_frame, text=class_amount_question, style="BlackSmall.TLabel")
            lbl_quan_class.grid(column=0, row=14, columnspan=3, sticky="w", pady=(10, 10))  # text positioning
        # Entry box to enter how many additional graduate courses the student is taking

        # Displays "Leveling Courses and Pre-requisites from Admission Letter:" title in file (bold)

        # Displays instructions to select disposition of uncompleted pre-reqs from degree plan
        pre_req_prompt = "Select Student's Prerequisite Course(s) Disposition:"
        lbl_pre_req = ttk.Label(scrollable_frame, text=pre_req_prompt, style="BlackSmall.TLabel")
        lbl_pre_req.grid(column=0, row=15, columnspan=4, sticky="ew", pady=(10, 0))  # text positioning

        # User prompted to select disposition of all uncompleted pre-reqs from degree plan on the screen
        dp_pre_req_class = []
        disp_select_one = tk.StringVar(scrollable_frame)
        disp_options = ["Completed", "Waived", "Not required by plan or elective", "Other"]
        row_index = 16
        # for pre_req_class in dp_pre_req_class
        #   lbl_disp_class = ttk.Label(scrollable_frame, text=pre_req_class, style="Black_txt.TLabel")
        #   lbl_disp_class.grid(column=0, row=row_index, columnspan=1, sticky="w", pady=(10, 0))  # text positioning
        #   option_menu = ttk.OptionMenu(
        #       scrollable_frame,
        #       disp_select_one,
        #       default=None,
        #       *dp_pre_req_class)
        #   option_menu.grid(column=1, row=row_index, columnspan=3, sticky="w", pady=(10, 0))
        #   row_index = row_index+1
        # (7 rowws, adjust w/ if statement and/or for loop: access var in [] + print check it, )
        # figur out the none thing, have disp_selct_one be sent to some sort of [] to avoid override vari
        # if statement detect if completed or waived/other/blank/none to get entry box open+sem of completion

        # Displays Course (Name & Number e.g. CS 6000) and selected disposition of uncompleted pre-reqs in file
        # display course abbrev and #: disposition
        # waiting on teammates for this section for what courses are pre-req's?
        # Completed: This must be followed by semester of completion (this info would appear on transcript)
        # Waived+other: should have a field where the user can enter either a semester or a short comment
        # it should be "None" if there's no uncompleted pre-reqs (check if user selected none/no options)

        # Displays "Outstanding Requirements:" title to file and screen
        lbl_gpa_req = ttk.Label(scrollable_frame, text="Outstanding Requirements:", style="BlackSmall.TLabel")
        lbl_gpa_req.grid(column=0, row=42, columnspan=2, sticky="w", pady=(10, 5))  # text positioning

        # Displays outstanding core, elective, and overall gpa requirements on screen
        # core_gpa_req = ""
        # elective_gpa_req = ""
        # overall_gpa_req = ""
        # maintain_core_gpa = ""
        # maintain_elective_gpa = ""
        # maintain_overall_gpa = ""
        # (waiting on akelanda for the above info)
        # lbl_core_gpa_req = ttk.Label(scrollable_frame, text=maintain_core_gpa, style="Black_txt.TLabel")
        # lbl_core_gpa_req.grid(column=0, row=43, columnspan=3, sticky="w", pady=(0, 5))  # text positioning
        # lbl_core_gpa_req = ttk.Label(scrollable_frame, text=core_gpa_req, style="Black_txt.TLabel")
        # lbl_core_gpa_req.grid(column=0, row=44, columnspan=3, sticky="w", pady=(0, 5))  # text positioning
        # lbl_elective_gpa_req = ttk.Label(scrollable_frame, text=maintain_elective_gpa, style="Black_txt.TLabel")
        # lbl_elective_gpa_req.grid(column=0, row=45, columnspan=3, sticky="w", pady=(0, 5))  # text positioning
        # lbl_elective_gpa_req = ttk.Label(scrollable_frame, text=elective_gpa_req, style="Black_txt.TLabel")
        # lbl_elective_gpa_req.grid(column=0, row=46, columnspan=3, sticky="w", pady=(0, 5))  # text positioning
        # lbl_overall_gpa_req = ttk.Label(scrollable_frame, text=maintain_overall_gpa, style="Black_txt.TLabel")
        # lbl_overall_gpa_req.grid(column=0, row=47, columnspan=3, sticky="w", pady=(0, 5))  # text positioning
        # lbl_overall_gpa_req = ttk.Label(scrollable_frame, text=overall_gpa_req, style="Black_txt.TLabel")
        # lbl_overall_gpa_req.grid(column=0, row=48, columnspan=3, sticky="w", pady=(0, 5))  # text positioning
        # waiting on akelanda for this section

        # Displays outstanding core, elective, and overall gpa requirements in file
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

        # currently being revamped/in progress
        # if os.name == 'posix':
        #   audit_filename = filedialog.asksaveasfile(initialdir="/", title="Open")
        # else:
        #   audit_filename = filedialog.asksaveasfilename(initialdir="\\", title="Open", filetypes=file_types)
