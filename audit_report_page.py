import tkinter as tk
import os
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox as mbox
from docx import Document


class AuditReportPage(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller

        # Handles gui for audit report page
        self.style = ttk.Style(self)
        self.style.configure("aud_report_gui.TFrame", background="white")
        self.style.configure("BlWht.TLabel", font=("Segoe UI", 20), foreground="black", background="white")
        self.style.configure("BlackSmall.TLabel", font=("Arial", 14), foreground="black", background="orange")
        self.style.configure("instruct_txt.TLabel", font=("Georgia", 14), foreground="black", background="orange")
        self.style.configure("Black_txt.TLabel", font=("Calibri", 14), foreground="black", background="yellow")
        self.style.configure("gray_subtext.TLabel", font=("Calibri", 12), foreground="gray", background="yellow")
        self.style.configure("input.TRadiobutton", background="pink")
        self.style.configure("data.TEntry", background="black")

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
        self.scrollable_frame = ttk.Frame(canvas, style="aud_report_gui.TFrame")
        self.scrollable_frame["padding"] = (5, 0, 5, 0)  # adds padding for spacing aesthetic

        # Scrollable frame page space distribution
        for row_index in range(49):
            self.scrollable_frame.grid_rowconfigure(row_index, weight=1)
        for col_index in range(15):
            self.scrollable_frame.grid_columnconfigure(col_index, weight=1)

        # Canvas Design and expansion when window expands
        canvas_win = canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")  # positioning
        canvas.bind('<Configure>', lambda e: canvas.itemconfig(canvas_win, width=e.width))
        self.scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.configure(yscrollcommand=scrollbar.set)  # sets scrollbar

        # Handles scrolling the frame based on OS when hovering over the scrollbar
        if os.name == "posix":
            self.scrollable_frame.bind("<Enter>", lambda e: self.scrollable_frame.bind_all('<MouseWheel>',  canvas.yview_scroll(int(e.delta), "units")))
            self.scrollable_frame.bind("<Leave>", lambda e: self.scrollable_frame.unbind_all('<MouseWheel>'))
        else:
            self.scrollable_frame.bind("<Enter>", lambda e: self.scrollable_frame.bind_all('<MouseWheel>', canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")))
            self.scrollable_frame.bind("<Leave>", lambda e: self.scrollable_frame.unbind_all('<MouseWheel>'))

        # Audit Report page title and design
        lbl_aud_report = ttk.Label(self.scrollable_frame, text="Audit Report", style="BlWht.TLabel")
        lbl_aud_report.grid(column=1, row=0, columnspan=2, sticky="nw", pady=(5, 0))  # text positioning

        document = Document()  # sets up Word doc object to generate audit report

        # Displays "Audit Report" title sent in file (centered, bolded & calibri font size 14)
        # ap_title = "Audit Report"

        # Displays student information in file
        # self.student_name = ""
        # self.student_id = ""
        # self.student_plan = "Master"
        # self.student_major = ""
        # self.student_track = ""
        # Name: (r1 left side, title bold, calibri 12)
        # ID: (r1 right side (but has the align left option chosen), title bold, calibri 12)
        # Plan: Master (r2 Left Side, title bold, calibri 12)
        # Major: (r2 right side (but has the align left option chosen), title bold, calibri 12)
        # Track: (r3 right side (but has the align left option chosen), based on degree plan, title bold, calibri 12)

        # Displays core, elective, and overall gpa label on screen
        lbl_core_gpa = ttk.Label(self.scrollable_frame, text="Core GPA: ", style="BlackSmall.TLabel")
        lbl_core_gpa.grid(column=0, row=6, columnspan=1, sticky="w", pady=(20, 0))  # text positioning
        lbl_elective_gpa = ttk.Label(self.scrollable_frame, text="Elective GPA: ", style="BlackSmall.TLabel")
        lbl_elective_gpa.grid(column=0, row=7, columnspan=1, sticky="w")  # text positioning
        lbl_overall_gpa = ttk.Label(self.scrollable_frame, text="Overall GPA: ", style="BlackSmall.TLabel")
        lbl_overall_gpa.grid(column=0, row=8, columnspan=1, sticky="w", pady=(0, 20))  # text positioning

        # Displays core, elective, and overall gpa on screen
        self.core_gpa = ""
        self.elective_gpa = ""
        self.overall_gpa = ""
        lbl_core_gpa_display = ttk.Label(self.scrollable_frame, text=self.core_gpa, style="Black_txt.TLabel")
        lbl_core_gpa_display.grid(column=1, row=6, columnspan=1, sticky="w", pady=(20, 0))  # text positioning
        lbl_elective_gpa_display = ttk.Label(self.scrollable_frame, text=self.elective_gpa, style="Black_txt.TLabel")
        lbl_elective_gpa_display.grid(column=1, row=7, columnspan=1, sticky="w")  # text positioning
        lbl_overall_gpa_display = ttk.Label(self.scrollable_frame, text=self.overall_gpa, style="Black_txt.TLabel")
        lbl_overall_gpa_display.grid(column=1, row=8, columnspan=1, sticky="w", pady=(0, 20))  # text positioning
        # waiting on akelanda to provide gpa variable data for this section

        # Displays core, elective, and overall gpa in file
        # Displays "Core GPA" row in file (r1, title bold, calibri 12)
        # Displays "Elective GPA" row in file (r2, title bold, calibri 12)
        # Displays "Overall GPA" row in fil (r3, title bold, calibri 12)
        # waiting on akelanda to finish making a way for me to access their gpa calculation answers

        # Displays "Core Courses" row in file (title bold, calibri 12)
        # self.core_courses = ""
        # Displays "Elective Courses" row in file (in course number order, title bold, calibri 12)
        # self.elective_courses = ""
        # waiting on sujay to provide the string variable that holds the line of text to print

        # Prompts user to answer questions label and design
        prompt_user_instruct = "Answer the Following Questions:"
        lbl_xtra_elect_prompt = ttk.Label(self.scrollable_frame, text=prompt_user_instruct, style="instruct_txt.TLabel")
        lbl_xtra_elect_prompt.grid(column=0, row=11, columnspan=2, sticky="w", pady=(20, 0))  # positioning

        # Asks user if student will be taking extra electives (used for elective gpa calculations)
        elective_question = "Student taking extra electives:"
        lbl_xtra_elect = ttk.Label(self.scrollable_frame, text=elective_question, style="BlackSmall.TLabel")
        lbl_xtra_elect.grid(column=0, row=12, columnspan=2, sticky="w", pady=(10, 0))  # positioning

        # Taking Extra Electives question (yes/no) selection options
        self.select_elective = tk.IntVar()
        self.xtra_elective_result = ""
        elective_confirm = ttk.Radiobutton(
            self.scrollable_frame,
            text="Yes",
            value=1,
            variable=self.select_elective,
            command=self.xtra_elective_question_value,
            style="input.TRadiobutton"
        )
        elective_confirm.grid(column=2, row=12, columnspan=1, sticky="w", pady=(10, 0))  # positioning
        elective_deny = ttk.Radiobutton(
            self.scrollable_frame,
            text="No",
            value=2,
            variable=self.select_elective,
            command=self.xtra_elective_question_value,
            style="input.TRadiobutton"
        )
        elective_deny.grid(column=3, row=12, columnspan=1, sticky="w", pady=(10, 0))  # positioning

        # Asks user if student is taking additional graduate courses and how many (used for gpa calculations)
        grad_course_question = "Student taking additional graduate courses:"
        lbl_grad_class = ttk.Label(self.scrollable_frame, text=grad_course_question, style="BlackSmall.TLabel")
        lbl_grad_class.grid(column=0, row=13, columnspan=3, sticky="w", pady=(20, 0))  # text positioning

        # Taking Additional Graduate Courses (yes/no) question selection options
        self.select_addi_class = tk.IntVar()
        self.addi_course_question_result = ""
        self.class_quantity = tk.StringVar()
        self.class_quantity_output = ""
        addi_courses_confirm = ttk.Radiobutton(
            self.scrollable_frame,
            text="Yes",
            value=1,
            variable=self.select_addi_class,
            command=self.addi_course_question_value,
            style="input.TRadiobutton"
        )
        addi_courses_confirm.grid(column=3, row=13, columnspan=1, sticky="w", pady=(20, 0))  # positioning
        addi_courses_deny = ttk.Radiobutton(
            self.scrollable_frame,
            text="No",
            value=2,
            variable=self.select_addi_class,
            command=self.addi_course_question_value,
            style="input.TRadiobutton"
        )
        addi_courses_deny.grid(column=3, row=13, columnspan=1, sticky="e", pady=(20, 0))  # positioning

        # Displays "Outstanding Requirements:" title to file and screen
        lbl_gpa_req = ttk.Label(self.scrollable_frame, text="Outstanding Requirements:", style="BlackSmall.TLabel")
        lbl_gpa_req.grid(column=0, row=15, columnspan=2, sticky="w", pady=(30, 5))  # text positioning

        # Displays outstanding core, elective, and overall gpa requirements information on screen
        self.maintain_core_gpa = ""
        self.maintain_elective_gpa = ""
        self.maintain_overall_gpa = ""
        self.core_gpa_req = ""
        self.elective_gpa_req = ""
        self.overall_gpa_req = ""
        lbl_core_gpa_req = ttk.Label(self.scrollable_frame, text=self.maintain_core_gpa, style="Black_txt.TLabel")
        lbl_core_gpa_req.grid(column=0, row=16, columnspan=2, sticky="w", pady=(0, 5))  # text positioning
        lbl_core_gpa_pass = ttk.Label(self.scrollable_frame, text=self.core_gpa_req, style="Black_txt.TLabel")
        lbl_core_gpa_pass.grid(column=0, row=17, columnspan=15, sticky="w", pady=(0, 20))  # text positioning
        lbl_elective_gpa_req = ttk.Label(self.scrollable_frame, text=self.maintain_elective_gpa, style="Black_txt.TLabel")
        lbl_elective_gpa_req.grid(column=0, row=18, columnspan=2, sticky="w", pady=(0, 5))  # text positioning
        lbl_elective_gpa_pass = ttk.Label(self.scrollable_frame, text=self.elective_gpa_req, style="Black_txt.TLabel")
        lbl_elective_gpa_pass.grid(column=0, row=19, columnspan=15, sticky="w", pady=(0, 20))  # text positioning
        lbl_overall_gpa_req = ttk.Label(self.scrollable_frame, text=self.maintain_overall_gpa, style="Black_txt.TLabel")
        lbl_overall_gpa_req.grid(column=0, row=20, columnspan=2, sticky="w", pady=(0, 5))  # text positioning
        lbl_overall_gpa_pass = ttk.Label(self.scrollable_frame, text=self.overall_gpa_req, style="Black_txt.TLabel")
        lbl_overall_gpa_pass.grid(column=0, row=21, columnspan=15, sticky="w", pady=(0, 20))  # text positioning
        # waiting on akelanda to provide me the string variable that has text line that they want me to print

        # Displays outstanding core, elective, and overall gpa requirements in file (Calibri size 12 font)
        # requirements that akelanda would follow for their part of the code:
        #   If GPA needed in remaining course(s) is >= 2.00:
        #   then, if one course remaining display: The student needs >= C+, B-, etc. in CS xxxx
        #   or if multiple courses remaining display: The student needs a GPA >= x.xx in: CS xxxx, CS xxxx, etc.
        #   If GPA needed in remaining course(s) is < 2.00: Display: The student must pass CS xxxx, CS xxxx, etc.
        #   or if the course completed then e.g. Core Complete.
        #   To graduate the student must have a Core GPA >= 3.19.
        #   or to graduate with a 3.0 <= Core GPA < 3.19 if they complete an extra 6000+ level CS/SE course.
        #   To graduate the student must have an overall + elective GPA >= 3.00.
        #   Adds with indents for the "the student" lines of section?
        # waiting on akelanda to provide me the string variable that has text line that they want me to print

        # Displays "Leveling Courses and Pre-requisites from Admission Letter:" title in file (bold, calibri 12)
        # pre_req_sect_title = "Leveling Courses and Pre-requisites from Admission Letter:"

        # Displays instructions to select disposition of pre-reqs from degree plan
        pre_req_prompt = "Select Student's Prerequisite Course(s) Disposition:"
        lbl_pre_req = ttk.Label(self.scrollable_frame, text=pre_req_prompt, style="instruct_txt.TLabel")
        lbl_pre_req.grid(column=0, row=22, columnspan=4, sticky="ew", pady=(30, 5))  # text positioning

        # User prompted to select disposition of pre-reqs from degree plan via the UI's drop down menu
        self.dp_pre_req_class = []
        disp_select_one = tk.StringVar(self.scrollable_frame)
        disp_options = ["Completed", "Waived", "Not required by plan or elective", "Other"]
        # row_index = 16
        # for pre_req_class in self.dp_pre_req_class
        #   lbl_disp_class = ttk.Label(self.scrollable_frame, textvariable=pre_req_class, style="Black_txt.TLabel")
        #   lbl_disp_class.grid(column=0, row=row_index, columnspan=1, sticky="w", pady=(10, 0))  # text positioning
        #   option_menu = ttk.OptionMenu(
        #       self.scrollable_frame,
        #       disp_select_one,
        #       default=None,
        #       *dp_pre_req_class)
        #   option_menu.grid(column=1, row=row_index, columnspan=3, sticky="w", pady=(10, 0))
        #   row_index = row_index+1
        # (9 rows, adjust w/ if statement and/or for loop: access var in [] + print check it, )
        # figur out the none thing, have disp_selct_one be sent to some sort of [] to avoid override vari
        # the "if statement" detects if it's completed or waived/other/blank/none to get entry box open+sem of completion
        # (self. disp dict+entry txt if you want word doc to be sep function)
        # maybe some tkinter entry event binding?
        #
        # e.g. but subj to change pre-req:
        # CS 3341 Probability & Statistics in CS and SE
        # CS 5303 Computer Science I
        # CS 5330 Computer Science II
        # CS 5333 Discrete Structures
        # CS 5343 Algorithm Analysis & Data Structures
        # CS 5348 Operating System Concepts
        # CS 5349 Automata Theory
        # CS 5354 Software Engineering
        # CS 5390 Computer Networks
        # Completed: This must be followed by semester of completion (this info would appear on transcript)
        # Waived+other: should have a field where the user can enter either a semester or a short comment
        # "None" if there's no uncompleted pre-reqs (check if user selected none/no options)
        # deal with row weight configure with each iteration of for loop
        # waiting on sujay for list/dictionary of pre-req courses to print them out in a list in the gui, and file

        # Displays Course (Name & Number e.g. CS 6000) and user selected disposition of pre-reqs in file (Calibri 12)
        # display [course abbrev and #]: [user selected disposition option] - [additional text, if applicable]
        # If user selected the "Completed" Disposition option: additionally display sem. of completion + grade in file
        # If user selected "Waived/Other" disposition option: additionally display user inputted comment/sem. in file
        # Display "None" if there's no uncompleted pre-reqs in file
        # waiting on sujay for list/dictionary of pre-req courses to print them out in a list in the gui, and file

        # Previous Page button and design
        prev_btn = ttk.Button(
            self.scrollable_frame,
            text="<< Previous",
            command=lambda: self.controller.show_frame("DegreePlanReportPage")
        )
        prev_btn.grid(column=0, row=49, columnspan=1, sticky="sw", padx=(5, 0), pady=(20, 20))  # button positioning

        # Saves printable audit report in File Explorer
        audit_report_btn = ttk.Button(
            self.scrollable_frame,
            text="Save Audit Report",
            command=lambda: self.save_file()
        )
        audit_report_btn.grid(column=3, row=49, columnspan=1, sticky="sw", padx=(0, 5), pady=(20, 20))  # positioning

        # Go to homepage button and design
        homepage_btn = ttk.Button(
            self.scrollable_frame,
            text="Go to Homepage",
            command=lambda: self.controller.show_frame("HomepageStart")
        )
        homepage_btn.grid(column=4, row=49, columnspan=1, sticky="se", pady=(20, 20))  # positioning

    # Saves value of Taking Extra Elective Question selection
    def xtra_elective_question_value(self):
        self.xtra_elective_result = self.select_elective.get()  # saves user selection of question

    # Asks user for Additional Graduate Courses quantity if user selected yes to additional graduate courses question
    def addi_course_question_value(self):
        self.addi_course_question_result = self.select_addi_class.get()  # saves value of user selection
        class_amount_question = "If yes, enter additional graduate course quantity:"
        submit_quantity_entry = "[Press Enter to Submit]"

        # Prompts user for additional course quantity
        if self.select_addi_class.get() == 1:
            lbl_quan_class = ttk.Label(self.scrollable_frame, text=class_amount_question, style="Black_txt.TLabel")
            lbl_quan_class.grid(column=0, row=14, columnspan=3, sticky="w", pady=(5, 10))  # text positioning
            # Entry box to enter how many additional graduate courses the student is taking
            class_quantity_box = ttk.Entry(self.scrollable_frame, textvariable=self.class_quantity, style="data.TEntry")
            class_quantity_box.grid(column=3, row=14, columnspan=1, sticky="w", pady=(5, 10))  # positioning
            class_quantity_box.bind("<Return>", self.addi_course_entry)  # saves entry upon user pressing enter
            # Prompts user to press enter to save their entry
            lbl_press_enter = ttk.Label(self.scrollable_frame, text=submit_quantity_entry, style="gray_subtext.TLabel")
            lbl_press_enter.grid(column=4, row=14, columnspan=2, sticky="w", pady=(5, 10))  # text positioning

    # Saves value entered in additional graduate course text entry box
    def addi_course_entry(self):
        self.class_quantity_output = self.class_quantity.get()
        print(self.class_quantity_output)

    # Opens File Explorer to save file
    def save_file(self):
        default_file_name = "audit_report"
        word_doc = "Microsoft Word Document"
        file_types = [(word_doc, "*.docx*"), ("All Files", "*.*")]
        save_file_progress = "Download Complete."

        # Opens File Explorer based on OS
        if os.name == 'posix':
            audit_report_filepath = asksaveasfilename(
                initialdir="/",
                title="Save As",
                # defaultextension=".docx", # not sure if this line works on mac OS?
                initialfile=default_file_name)
            # Checks if user pressed Save or Cancel button
            if not audit_report_filepath:
                mbox.showerror("Error", "File Not Saved. Please, try Again.")  # file not saved error message
            else:
                self.generate_report_content(audit_report_filepath)  # calls function to write text to file
                # Displays message to user that the file is being saved
                mbox.showinfo("Information", save_file_progress)
        else:
            audit_report_filepath = asksaveasfilename(
                defaultextension=".docx",
                filetypes=file_types,
                initialdir="\\",
                initialfile=default_file_name,
                title="Save As")
            # Checks if user pressed cancel or save in file explorer
            if not audit_report_filepath:
                mbox.showerror("Error", "File Not Saved. Please, try Again.")  # file not saved error message
            else:
                self.generate_report_content(audit_report_filepath)  # calls function to write text to file
                # Displays message to user that the file is being saved
                mbox.showinfo("Information", save_file_progress)

            # this method is in progress/being revamped at the moment

    # Writes information to audit report file
    def generate_report_content(self, audit_report_filepath):
        # [note to self: move the Word doc related stuff here]
        # Creates a file using given filename
        # with open(audit_report_filepath, "w") as f:

        print(audit_report_filepath)
        # this method is in progress/being revamped at the moment
