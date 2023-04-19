import tkinter as tk
from tkinter import *
from tkinter import ttk


class DegreePlanPage(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller  # allows for switching between application pages

        # Handles Degree Plan page style options
        style = ttk.Style(self)
        style.configure("dp_gui.TFrame", background="black", relief="flat")
        style.configure("section.TFrame", background="orange", relief="raised")
        style.configure("sub_section.TFrame", background="orange", relief="flat")
        
        style.configure("big_heading.TLabel", font=("Segoe print", 30, "bold"), foreground="black", background="orange")
        style.configure("medium_heading.TLabel", font=("Verdana", 25), foreground="black", background="orange")
        style.configure("small_heading.TLabel", font=("Verdana", 15), foreground="black", background="orange")

        style.configure("normal_text.TLabel", font=("Bookman Old Style", 14), foreground="black", background="orange")
        style.configure("filling_text.TLabel", font=("Bookman Old Style", 14), foreground="black", background="white", relief="sunken")
        style.configure("course_section.TLabel", font=("Bookman Old Style", 14), foreground="orange", background="black")

        style.configure("TRadiobutton", font=("Bookman Old Style", 14), foreground="black", background="orange", relief="flat")



        # style.configure("GuiTitle.TLabel", font=("Segoe UI", 25), foreground="black", background="orange")
        # style.configure("DegreeTitle.TLabel", font=("Segoe UI", 15), foreground="black", background="orange")
        # style.configure("BlSmall.TLabel", font=("Roboto", 14), foreground="black", background="white")
    
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
        # frame.grid(column=0, row=0, sticky="nsew")  # positioning
        frame.pack(expand=TRUE, fill=BOTH, side=TOP)

# Creating frame sections
# 0. Gui Title Frame
        fr_titleGui = ttk.Frame(frame, style="section.TFrame")
        fr_titleGui.columnconfigure(0, weight=1)
        fr_titleGui.rowconfigure(0, weight=1)   
        fr_titleGui.grid(column=0, row=0, sticky="nsew", pady=5)
      
        lbl_gui = ttk.Label(fr_titleGui, text="DEGREE PLAN EDITOR", style="big_heading.TLabel")
        lbl_gui.grid(column=0, row=0)  # text positioning

# Get student info function
## Need to check where should i get this information.
## from transcrip directly or from Aiden File
        def get_student_info():   
            major       = "Data Science" 
            name        = "Name 111111111111111"
            id          = "ID 1"
            sem_ad      = "Semester 111"

            return major, name, id, sem_ad
       
        std_major, std_name, std_id, std_sem_admitted = get_student_info()

# 1. Title Frame        
        c1=0
        r1=4
        fr_title = ttk.Frame(frame, style="section.TFrame")
        fr_title.columnconfigure(0, weight=1)
        for r in range(r1):
            fr_title.rowconfigure(r, weight=1)
        fr_title.grid(column=0, row=1, sticky="nsew", pady=5)   

        # Labeling
        lbl_title = ttk.Label(fr_title, text="DEGREE PLAN", style="medium_heading.TLabel")
        lbl_title.grid(column=0, row=0)
        lbl_title = ttk.Label(fr_title, text="UNIVERSITY OF TEXAS AT DALLAS", style="medium_heading.TLabel")
        lbl_title.grid(column=0, row=1)
        lbl_title = ttk.Label(fr_title, text="MASTER OF COMPUTER SCIENCE", style="medium_heading.TLabel")
        lbl_title.grid(column=0, row=2)

        # Get and Display Student's Major
        lbl_major = ttk.Label(fr_title, text=std_major, style="medium_heading.TLabel")
        lbl_major.grid(column=0, row=4)
       
# 2. Student Frame
        c2=5
        r2=3
        fr_student = ttk.Frame(frame, style="section.TFrame")
        for c in range(c2):
            fr_student.columnconfigure(c, weight=1)
        for r in range(r2):
            fr_student.rowconfigure(r, weight=1)
        fr_student.grid(column=0, row=2, sticky="nsew", pady=5)

        # Labeling 
        # Student Name
        lbl_student = ttk.Label(fr_student, text="Name of Student:", style="normal_text.TLabel")
        lbl_student.grid(column=0, row=0, sticky='w', padx=(10,0), po)

        lbl_student = ttk.Label(fr_student, text=std_name, style="filling_text.TLabel")
        lbl_student.grid(column=1, row=0, sticky='w', padx=(10,0))

        # Student ID
        lbl_student = ttk.Label(fr_student, text="Student ID Number:", style="normal_text.TLabel")
        lbl_student.grid(column=0, row=1, sticky='w', padx=(10,0))
   
        lbl_student = ttk.Label(fr_student, text=std_id, style="filling_text.TLabel")
        lbl_student.grid(column=1, row=1, sticky='w', padx=(10,0))

        # Semester Additted
        lbl_student = ttk.Label(fr_student, text="Semester Admitted to Program:", style="normal_text.TLabel")
        lbl_student.grid(column=0, row=2, sticky='w', padx=(10,0))
   
        lbl_student = ttk.Label(fr_student, text=std_sem_admitted, style="filling_text.TLabel")
        lbl_student.grid(column=1, row=2, sticky='w', padx=(10,0))
 
        # FT, Thesis, Anticipated
# # Need to do something after FT and Thesis was selected
#         def yes_no(c_index, r_index):
#             selected_value = tk.StringVar()
#             options = (   ('Yes', 'Y'),
#                     ('No', 'N'))
#             for opt in options:
#                 r = ttk.Radiobutton(                        
#                                 fr_student,
#                                 text=opt[0],
#                                 value=opt[1],
#                                 variable=selected_value,
#                                 style="TRadiobutton"
#                 )
#                 r.grid(column=c_index, row=r_index, sticky='w', padx=(10,0))
#                 c_index += 1

#         # Fast Track
#         lbl_student = ttk.Label(fr_student, text="FT:", style="normal_text.TLabel")
#         lbl_student.grid(column=2, row=0, sticky='w', padx=(10,0))
#         yes_no(3, 0)

#         # Thesis
#         lbl_student = ttk.Label(fr_student, text="Thesis:", style="normal_text.TLabel")
#         lbl_student.grid(column=2, row=1, sticky='w', padx=(10,0))
#         yes_no(3, 1)

#         # Anticipated Graduation
# # need to save this info somewhere for Degree Plan Report Later
#         lbl_student = ttk.Label(fr_student, text="Anticipated Graduation", style="normal_text.TLabel")
#         lbl_student.grid(column=2, row=2, sticky='w', padx=(10,0))

#         expect_grad = tk.StringVar()      
#         entry_student = ttk.Entry(fr_student, text=expect_grad, font=("Bookman Old Style", 14), foreground="black")
#         entry_student.grid(column=3, row=2, sticky='w', columnspan=2)


# # 3. Courses Frame
#         c3=5
#         r3=50 # Need edit later, maybe some more extra line so auditor can manually add more cores if needed
#         fr_course = ttk.Frame(frame, style="section.TFrame")
#         for c in range(c3):
#             fr_course.columnconfigure(c, weight=1)
#         for r in range(r3):
#             fr_course.rowconfigure(r, weight=1)
#         fr_course.grid(column=0, row=3, sticky="nsew", pady=5)

#         # Labling Header
#         lbl_course= ttk.Label(fr_course, text="Course Title", style="normal_text.TLabel")
#         lbl_course.grid(column=0, row=0, sticky='w', padx=(10,0), pady=(10,0))

#         lbl_course= ttk.Label(fr_course, text="Course Number", style="normal_text.TLabel")
#         lbl_course.grid(column=1, row=0, sticky='w', pady=(10,0))
        
#         lbl_course= ttk.Label(fr_course, text="UTD Semester", style="normal_text.TLabel")
#         lbl_course.grid(column=2, row=0, sticky='w', pady=(10,0))

#         lbl_course= ttk.Label(fr_course, text="Transfer", style="normal_text.TLabel")
#         lbl_course.grid(column=3, row=0, sticky='w', pady=(10,0))

#         lbl_course= ttk.Label(fr_course, text="Grade", style="normal_text.TLabel")
#         lbl_course.grid(column=4, row=0, sticky='w', pady=(10,0))

#         # Labeling CORE COURSES Info
#         lbl_course= ttk.Label(fr_course, text="CORE COURSES \t\t (15 Credit Hours) \t\t 3.19 Grade Point Average Required", style="course_section.TLabel")
#         lbl_course.grid(column=0, row=1, columnspan=5, pady=(10,10), padx=(10,0))

#         # Function to auto fill dummmy course row by row
#         def auto_course_lable(course_info, at_row):
#             c = 0
#             for e in course_info:
#                 lbl_course= ttk.Label(fr_course, text=e, style="normal_text.TLabel")
#                 lbl_course.grid(column=c, row=at_row, sticky='w', padx=(10,0))
#                 c += 1

#         course_info = ["Natural Language Processing",
#                        "CS 6320", 
#                        "22F", 
#                        "20F" ,
#                        "B+"]
#         auto_course_lable(course_info, 2)
#         auto_course_lable(course_info, 3)
#         auto_course_lable(course_info, 4)
#         auto_course_lable(course_info, 5)
        

#         # Labeling 1 of 5 CORE COURSES
#         lbl_course= ttk.Label(fr_course, text="One of the following Five Core Courses", style="course_section.TLabel")
#         lbl_course.grid(column=0, row=6, columnspan=5, pady=(10,10), padx=(10,0))

#         auto_course_lable(course_info, 7)
#         auto_course_lable(course_info, 8)
#         auto_course_lable(course_info, 9)
#         auto_course_lable(course_info, 10)
#         auto_course_lable(course_info, 11)


#         # Labeling 6000 LEVEL ELECTIVE
#         lbl_course= ttk.Label(fr_course, text="FIVE APPROVED 6000 LEVEL ElECTIVES \t\t (15* Credit Hours) \t\t 3.0 Grade Point Average Required", 
#                               style="course_section.TLabel")
#         lbl_course.grid(column=0, row=12, columnspan=5, pady=(10,10), padx=(30,0))


#         course_info1 = ["Select from Drop Box",
#                        "Auto match", 
#                        "22F", 
#                        "20F" ,
#                        "B+"]
#         auto_course_lable(course_info1, 13)
#         auto_course_lable(course_info1, 14)
#         auto_course_lable(course_info1, 15)
#         auto_course_lable(course_info1, 16)
#         auto_course_lable(course_info1, 17)

#         # Labeling Additional Electtive
#         lbl_course= ttk.Label(fr_course, text="Additional Elective (3 Credits Hours Mimimum)", 
#                               style="course_section.TLabel")
#         lbl_course.grid(column=0, row=18, columnspan=5, pady=(10,10), padx=(30,0))
        
       

# # 4. Note, Advisor, Date Frame
#         c4=4
#         r4=4
#         fr_note = ttk.Frame(frame, style="section.TFrame")
#         for c in range(c4):
#             fr_note.columnconfigure(c, weight=1)
#         for r in range(r4):
#             fr_note.rowconfigure(r, weight=1)
#         fr_note.grid(column=0, row=4, sticky="nsew", pady=5)

#          # Labeling note
# # Should i hard code note or get info depend on which major.
# # Need to talk to Aleky and Aiden about it
#         lbl_note= ttk.Label(fr_note, text="* May include any 6000 or 7000 level CS course with prior permission", style="normal_text.TLabel")
#         lbl_note.grid(column=0, row=1, columnspan=5, pady=(10,10), padx=(10,0))

#         # Labeling Advisor, Create Entry
#         lbl_note = ttk.Label(fr_note, text="Academic Advisor", style="normal_text.TLabel")
#         lbl_note.grid(column=0, row=3, sticky='w', padx=10, pady=10)

#         advisor_name = tk.StringVar()      
#         entry_note = ttk.Entry(fr_note, text=advisor_name, font=("Bookman Old Style", 14), foreground="black")
#         entry_note.grid(column=1, row=3, sticky='w', pady=10)

#  # Labeling Advisor, Create Entry
#         lbl_note = ttk.Label(fr_note, text="Date Submitted", style="normal_text.TLabel")
#         lbl_note.grid(column=2, row=3, sticky='w', padx=(10,0))

#         advisor_name = tk.StringVar()      
#         entry_note = ttk.Entry(fr_note, text=advisor_name, font=("Bookman Old Style", 14), foreground="black")
#         entry_note.grid(column=3, row=3, sticky='w', pady=10)

        



# # 5. Linkup Frame
#         linkup_row = 5
#         fr_link= ttk.Frame(frame, style="section.TFrame")
#         fr_link.columnconfigure(0, weight=1)
#         fr_link.rowconfigure(0, weight=1)
#         fr_link.grid(column=0, row=linkup_row, sticky="nsew", pady=5)  


#     # #     # Choose student's degree plan track text label and design
#     # #     # lbl_dp_track = ttk.Label(frame, text="Choose student's chosen track/Degree Plan:", style="BlSmall.TLabel")
#     # #     # lbl_dp_track.grid(column=1, row=1, columnspan=1, padx=5, pady=10)  # text positioning

#     # #     # Insert here a Degree Plan Track options list, where the user can add/select/change/remove tracks?

#     # #     # Insert here a list of prerequisite courses, where the user can change/delete/add new/add to degree plan?

#     # #     # save what track option was selected in a way that the audit report can access it

#     # #     # Insert here a way for user to select if the student is doing Fast Track, and save value to student object?

#     # #     # Insert here a way for user to select if the student is doing Thesis, and save value to student object?

#     # #     # Insert here way for user to generate, update with all info & save where user wants to save student object?

#         # Previous Page button and design
#         prev_btn = ttk.Button(
#             fr_link,
#             text="<< Previous",
#             command=lambda: self.controller.show_frame("UploadFilePage")
#         )
#         prev_btn.grid(column=0, row=linkup_row, columnspan=1, sticky="sw", pady=20)  # button positioning

#         # Button to direct user to degree_plan_report_page.py in order for user to edit degree plan
#         next_btn = ttk.Button(
#             fr_link,
#             text="Next >>",
#             command=lambda: controller.show_frame("DegreePlanReportPage")
#         )
#         next_btn.grid(column=0, row=linkup_row, columnspan=1, sticky="se", pady=20)  # button padding

#     # note to the developer in charge of the degree plan gui:
#     # This file is just to get, whoever is working on the Degree Plan GUI, a head start on the gui.
#     # there's still the rest of the gui, student object stuff, etc. that you'll need to figure out and add to this
#     # modify it as much as you want to, just make sure to:
#     # include a way for audit_report_page.py to know what degree plan track and prerequisite courses are chosen
