import tkinter as tk
import os
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox as mbox
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

        # Displays outstanding core, elective, and overall gpa requirements information lines on screen
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

        # Displays instructions to select disposition of pre-reqs from degree plan
        pre_req_prompt = "Select Disposition for each Leveling Course(s) & Prerequisite(s):"
        lbl_pre_req = ttk.Label(self.scrollable_frame, text=pre_req_prompt, style="instruct_txt.TLabel")
        lbl_pre_req.grid(column=0, row=22, columnspan=6, sticky="ew", pady=(30, 0))  # text positioning

        # Displays instructions to select None if there's no prerequisite or leveling course(s)
        none_choice_instruct = "Select None if there is no Prerequisite or Leveling course(s) from the Admission Letter"
        lbl_none_choice_instruct = ttk.Label(self.scrollable_frame, text=none_choice_instruct, style="gray_subtext.TLabel")
        lbl_none_choice_instruct.grid(column=0, row=23, columnspan=7, sticky="w", pady=(5, 5))  # positioning

        # User prompted to select disposition of pre-reqs from degree plan via the GUI's drop down menu
        self.row_count = 23  # holds row of menu & text
        self.disposition_dict = {
            "dp_pre_req_class": ["CS 3341", "CS 5303", "CS 5330", "CS 5333", "CS 5343", "CS 5348", "CS 5349", "CS 5354", "CS 5390"],
            "disp_options": ["None", "Completed", "Waived", "Not required by plan or elective", "Other"],
            "disp_selections": [],  # holds user selected disposition choice
            "opt_menu": [],  # holds disposition menu widget
            "user_course_comment": []  # Hold's user's entry in text entry box
        }
        for pre_req_class in self.disposition_dict["dp_pre_req_class"]:
            self.row_count += 1
            disp_select = tk.StringVar()  # holds user disposition selection
            disp_select.set(self.disposition_dict["disp_options"][0])  # sets default value of disposition
            disp_select.trace("w", self.disposition_update)  # updates saved disposition when user changes choice
            disp_comment = tk.StringVar()  # Holds user's text entry in text box
            # Displays classes on screen
            lbl_disp_class = ttk.Label(self.scrollable_frame, text=pre_req_class, style="Black_txt.TLabel")
            lbl_disp_class.grid(column=0, row=self.row_count, columnspan=1, sticky="w", pady=(10, 0))  # positioning
            # Displays drop down menu's on screen
            option_menu = ttk.OptionMenu(
                self.scrollable_frame,
                disp_select,
                self.disposition_dict["disp_options"][0],
                *self.disposition_dict["disp_options"])
            option_menu.grid(column=1, row=self.row_count, columnspan=3, sticky="w", pady=(10, 0))  # positioning
            self.disposition_dict["disp_selections"].append(disp_select)  # adds needed number of StringVar() to list
            self.disposition_dict["opt_menu"].append(option_menu)  # Adds disposition menu with unique variable to list
            self.disposition_dict["user_course_comment"].append(disp_comment)  # adds placement StringVar to list

        # Previous Page button and design
        prev_btn = ttk.Button(
            self.scrollable_frame,
            text="<< Previous",
            command=lambda: self.controller.show_frame("DegreePlanReportPage")
        )
        prev_btn.grid(column=0, row=self.row_count+1, columnspan=1, sticky="sw", padx=(5, 0), pady=(20, 20))  # positioning

        # Saves printable audit report in File Explorer
        audit_report_btn = ttk.Button(
            self.scrollable_frame,
            text="Save Audit Report",
            command=lambda: self.save_file()
        )
        audit_report_btn.grid(column=3, row=self.row_count+1, columnspan=1, sticky="sw", padx=(0, 5), pady=(20, 20))  # positioning

        # Go to homepage button and design
        homepage_btn = ttk.Button(
            self.scrollable_frame,
            text="Go to Homepage",
            command=lambda: self.controller.show_frame("HomepageStart")
        )
        homepage_btn.grid(column=4, row=self.row_count+1, columnspan=1, sticky="se", pady=(20, 20))  # positioning

    # Saves value of Taking Extra Elective Question selection
    def xtra_elective_question_value(self):
        self.xtra_elective_result = self.select_elective.get()  # saves "value" of user selection

    # Asks user for Additional Graduate Courses quantity if user selected yes to Additional Graduate Courses question
    def addi_course_question_value(self):
        self.addi_course_question_result = self.select_addi_class.get()  # saves value of user selection
        class_amount_question = "If yes, enter additional graduate course quantity:"
        submit_quantity_entry = "[Press Enter to Submit]"

        # Prompts user for additional course quantity
        if self.select_addi_class.get() == 1:
            lbl_quan_class = ttk.Label(self.scrollable_frame, text=class_amount_question, style="Black_txt.TLabel")
            lbl_quan_class.grid(column=0, row=14, columnspan=3, sticky="w", pady=(5, 10))  # text positioning
            # Entry text box for user to enter how many additional graduate courses the student is taking
            class_quantity_box = ttk.Entry(self.scrollable_frame, textvariable=self.class_quantity, style="data.TEntry")
            class_quantity_box.grid(column=3, row=14, columnspan=1, sticky="w", pady=(5, 10))  # positioning
            class_quantity_box.bind("<Return>", self.addi_course_entry)  # saves entry upon user press Enter
            # Displays instructions for user to press enter to save their entry
            lbl_press_enter = ttk.Label(self.scrollable_frame, text=submit_quantity_entry, style="gray_subtext.TLabel")
            lbl_press_enter.grid(column=4, row=14, columnspan=2, sticky="w", pady=(5, 10))  # positioning

    # Saves value entered in Additional Graduate Course text entry box upon the Enter key being pressed
    def addi_course_entry(self, event):
        self.class_quantity_output = self.class_quantity.get()

    # Updates saved user selected disposition values stored in list
    def disposition_update(self, *args):
        # for saved_disp in self.disposition_dict["disp_selections"]:
        #   print(saved_disp.get())
        print(self.disposition_dict["disp_options"][0])
        # entry_row = self.row_count+1
        # the "if statement" detects if it's completed/waived/other/none to get entry box open+sem of completion
        # self. disp entry txt, event binding, & save to self. list in dict via stringVar, remember dynamic rows
        # Completed: followed by semester of completion (info on transcript)
        # Waived+other: should have a field where the user can enter either a semester or a short comment
        # (check if user selected none/no opt)
        #             "user_course_comment": []  # Hold's user's entry in text entry box

    # Opens File Explorer to save file
    def save_file(self):
        default_file_name = "audit_report"
        word_doc = "Microsoft Word Document"
        file_types = [("All Files", "*.*"), (word_doc, "*.docx*"), ]
        save_file_progress = "Download Complete. Please check the audit report before exiting the program."

        # Opens File Explorer based on OS
        if os.name == 'posix':
            audit_report_filepath = asksaveasfilename(
                initialdir="/",
                title="Save As",
                defaultextension=".docx",
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

    # Writes information to audit report file
    def generate_report_content(self, audit_report_filepath):
        # Creates a file using given filename
        # with open(audit_report_filepath, "w") as f:

        print(audit_report_filepath)

        document = Document()  # sets up Word doc object to generate audit report

        # Displays "Audit Report" title sent in file (centered, bolded & calibri font size 14)
        # ap_title = "Audit Report"

        # Adds spacing between lines

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

        # Adds spacing between lines

        # Displays core, elective, and overall gpa in file
        # Displays "Core GPA" row in file (r1, title bold, calibri 12)
        # Displays "Elective GPA" row in file (r2, title bold, calibri 12)
        # Displays "Overall GPA" row in fil (r3, title bold, calibri 12)
        # waiting on akelanda to finish making a way for me to access their gpa calculation answers

        # Adds spacing between lines

        # Displays "Core Courses" row in file (title bold, calibri 12)
        # self.core_courses = ""
        # Displays "Elective Courses" row in file (in course number order, title bold, calibri 12)
        # self.elective_courses = ""
        # waiting on sujay to provide the string/list/dictionary that holds the line of text to print

        # Adds spacing between lines

        # Displays "Leveling Courses and Pre-requisites from Admission Letter:" title in file (bold, calibri 12)
        # pre_req_sect_title = "Leveling Courses and Pre-requisites from Admission Letter:"

        # Adds spacing between lines

        # Displays Course (Name & Number e.g. CS 5333) and user selected disposition of pre-reqs in file (Calibri 12)
        # display [course abbrev and #]: [user selected disposition option] - [additional text, if applicable]
        # use for loop w/ .get() to get value in dict's stringVar to append to new [] to write to word doc
        # disp_choice_print = []
        # for saved_disp in self.disposition_dict["disp_selections"]:
        #   final_disp = saved_disp.get()
        #   disp_choice_print.append(final_disp)
        # If user selected "Completed" disposition option: additionally display sem. of completion + grade in file
        # If user selected "Waived/Other" disposition option: additionally display user inputted comment/sem. in file
        # Display "None" if there's no uncompleted pre-reqs in file
        # note to self: look at sujay's gitHub for list/dict of pre-req to print them out in a list in the gui + file

        # Adds spacing between lines

        # Displays "Outstanding Requirements:" title in file (bold, calibri 12)
        # outstanding_req_title = "Outstanding Requirements:"

        # Adds spacing between lines

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

        # this method is in progress/being revamped at the moment
