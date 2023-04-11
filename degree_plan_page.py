import tkinter as tk
from tkinter import *
from tkinter import ttk


class DegreePlanPage(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller  # allows for switching between application pages

        # Handles Degree Plan page style options
        style = ttk.Style(self)
        style.configure("dp_gui.TFrame", background="black", relief="sunken")
        style.configure("section.TFrame", background="orange", relief="raised")
        
        style.configure("big_heading.TLabel", font=("Segoe print", 30, "bold"), foreground="black", background="orange")
        style.configure("medium_heading.TLabel", font=("Verdana", 25), foreground="black", background="orange")
        style.configure("small_heading.TLabel", font=("Verdana", 15), foreground="black", background="orange")

        style.configure("normal_text.TLabel", font=("Bookman Old Style", 14), foreground="black", background="orange")
        style.configure("filling_text.TLabel", font=("Bookman Old Style", 14), foreground="black", background="white", relief="ridge")

        style.configure("TRadiobutton", font=("Bookman Old Style", 14), foreground="black", background="orange", relief="flat")



        # style.configure("GuiTitle.TLabel", font=("Segoe UI", 25), foreground="black", background="orange")
        # style.configure("DegreeTitle.TLabel", font=("Segoe UI", 15), foreground="black", background="orange")
        # style.configure("BlSmall.TLabel", font=("Roboto", 14), foreground="black", background="white")
    
        # Handles frame expansion when application window is expanded
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        # Frame outline and design
        frame = ttk.Frame(self, style="dp_gui.TFrame")
        frame["padding"] = 10
        frame.columnconfigure(0, weight=1)
        section = 11
        for r in range(section):
            frame.rowconfigure(r, weight=1)
        # frame.grid(column=0, row=0, sticky="nsew")  # positioning
        frame.pack(expand=TRUE, fill=BOTH, side=TOP)

        # Creating frame sections
        #   0. Gui Title Frame
        fr_titleGui = ttk.Frame(frame, style="section.TFrame")
        fr_titleGui.columnconfigure(0, weight=1)
        fr_titleGui.rowconfigure(0, weight=1)   
        fr_titleGui.grid(column=0, row=0, sticky="nsew", padx=100, pady=5)
      

        lbl_gui = ttk.Label(fr_titleGui, text="DEGREE PLAN EDITOR", style="big_heading.TLabel")
        lbl_gui.grid(column=0, row=0)  # text positioning
       
#   1. Title Frame
        c1=0
        r1=4
        fr_title = ttk.Frame(frame, style="section.TFrame")
        fr_title.columnconfigure(0, weight=1)
        for r in range(r1):
            fr_title.rowconfigure(r, weight=1)
        fr_title.grid(column=0, row=1, sticky="nsew", pady=5)

 # Labeling
        lbl_title = ttk.Label(fr_title, text="DEGREE PLAN", style="medium_heading.TLabel")
        lbl_title.grid(column=0, row=0, padx=5, pady=5)
        lbl_title = ttk.Label(fr_title, text="UNIVERSITY OF TEXAS AT DALLAS", style="medium_heading.TLabel")
        # lbl_title.grid(column=0, row=1, padx=5, pady=5)
        lbl_title.grid(column=0, row=1)
        lbl_title = ttk.Label(fr_title, text="MASTER OF COMPUTER SCIENCE", style="medium_heading.TLabel")
        lbl_title.grid(column=0, row=2, padx=5, pady=5)

# Get and Display Student's Major
        major = "Data Science"  # Will pass a function to get major later
        lbl_major = ttk.Label(fr_title, text=major, style="medium_heading.TLabel")
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
        lbl_name = ttk.Label(fr_student, text="Name of Student:", style="normal_text.TLabel")
        lbl_name.grid(column=0, row=0, sticky='w', padx=(10,0))
        std_name = "Name 111111111111111"
        lbl_name = ttk.Label(fr_student, text=std_name, style="filling_text.TLabel")
        lbl_name.grid(column=1, row=0, sticky='w', padx=(10,0))
        # entry = Entry(fr_student, width=25)
        # entry.grid(column=1, row=1)

# Student ID
        lbl_name = ttk.Label(fr_student, text="Student ID Number:", style="normal_text.TLabel")
        lbl_name.grid(column=0, row=1, sticky='w', padx=(10,0))
        std_id = "ID 1"
        lbl_name = ttk.Label(fr_student, text=std_id, style="filling_text.TLabel")
        lbl_name.grid(column=1, row=1, sticky='w', padx=(10,0))

#  Semester Additted
        lbl_name = ttk.Label(fr_student, text="Semester Admitted to Program:", style="normal_text.TLabel")
        lbl_name.grid(column=0, row=2, sticky='w', padx=(10,0))
        sem_ad = "Semester 1"
        lbl_name = ttk.Label(fr_student, text=sem_ad, style="filling_text.TLabel")
        lbl_name.grid(column=1, row=2, sticky='w', padx=(10,0))

# FT and Thesis
        def yes_no(c_index, r_index):
            # print('Test yes_no')
            selected_value = tk.StringVar()
            sizes = (   ('Yes', 'S'),
                    ('No', 'M'))
            for size in sizes:
                r = ttk.Radiobutton(        
                                fr_student,
                                text=size[0],
                                value=size[1],
                                variable=selected_value,
                                style="TRadiobutton"
                )
                r.grid(column=c_index, row=r_index, sticky='w')
                c_index += 1

    # Fast Track
        lbl_name = ttk.Label(fr_student, text="FT:", style="normal_text.TLabel")
        lbl_name.grid(column=2, row=0, sticky='w', padx=(10,0))
        yes_no(3, 0)

    # Thesis
        lbl_name = ttk.Label(fr_student, text="Thesis:", style="normal_text.TLabel")
        lbl_name.grid(column=2, row=1, sticky='w', padx=(10,0))
        yes_no(3, 1)

# Anticipated Graduation
        lbl_name = ttk.Label(fr_student, text="Anticipated Graduation", style="normal_text.TLabel")
        lbl_name.grid(column=2, row=2, sticky='w', padx=(10,0))

        expect_grad = tk.StringVar()      
        entry_name = ttk.Entry(fr_student, text=expect_grad, font=("Bookman Old Style", 14), foreground="black")
        entry_name.grid(column=3, row=2, sticky='w', columnspan=2, padx=(10,10))
        # entry_name.focus()

        




        # e = Entry(root, width=50, borderwidth=5)
# e = Entry(root, width=50)
# e.pack()
# e.insert(0, "Enter Your Name:") # Default Text inside box



        # # 3. Core Frame
        # c3=0
        # r3=10
        # fr_core = ttk.Frame(frame, style="section.TFrame")
        # fr_core.columnconfigure(0, weight=1)
        # for r in range(r3):
        #     fr_core.rowconfigure(r, weight=1)
        # .columnconfigure(0, weight=1)
        # .rowconfigure(0, weight=1)
        # fr_core.grid(column=0, row=2, sticky="nsew")

        # # 4. Core_Option Frame
        # c4=0
        # r4=7
        # fr_coreOption = ttk.Frame(frame, style="section.TFrame")
        # fr_coreOption.columnconfigure(0, weight=1)
        # for r in range(r4):
        #     fr_coreOption.rowconfigure(r, weight=1)
        # fr_coreOption.grid(column=0, row=3, sticky="nsew")

    #     # # 5. Five Elective Frame
    #     # c5=0
    #     # r5=7
    #     # fr_elective = ttk.Frame(frame, style="section.TFrame")
    #     # fr_elective.columnconfigure(0, weight=1)
    #     # for r in range(r5):
    #     #     fr_elective.rowconfigure(r, weight=1)
    #     # fr_elective.grid(column=0, row=4, sticky="nsew")

    #     # # 6. Additional Elective Frame
    #     # c6=0
    #     # r6=7
    #     # fr_electiveAdd = ttk.Frame(frame, style="section.TFrame")
    #     # fr_electiveAdd.columnconfigure(0, weight=1)
    #     # for r in range(r6):
    #     #     fr_electiveAdd.rowconfigure(r, weight=1)
    #     # fr_elective.grid(column=0, row=5, sticky="nsew")

    #     # # 7. Other Requirement Frame
    #     # c7=0
    #     # r7=3
    #     # fr_otherReg = ttk.Frame(frame, style="section.TFrame")
    #     # fr_otherReg.columnconfigure(0, weight=1)
    #     # for r in range(r7):
    #     #     fr_otherReg.rowconfigure(r, weight=1)
    #     # fr_otherReg.grid(column=0, row=6, sticky="nsew")

    #     # # 8. Prerequisites Frame
    #     # c8=0
    #     # r8=3
    #     # fr_Prereq= ttk.Frame(frame, style="section.TFrame")
    #     # fr_Prereq.columnconfigure(0, weight=1)
    #     # for r in range(r8):
    #     #     fr_Prereq.rowconfigure(r, weight=1)
    #     # fr_Prereq.grid(column=0, row=7, sticky="nsew")

    #     # # 9. Note Frame
    #     # c9=0
    #     # r9=7
    #     # fr_note = ttk.Frame(frame, style="section.TFrame")
    #     # fr_note.columnconfigure(0, weight=1)
    #     # for r in range(7):
    #     #     fr_note.rowconfigure(r, weight=1)
    #     # fr_note.grid(column=0, row=6, sticky="nsew")

        #   10. Linkup Frame
        fr_link= ttk.Frame(frame, style="section.TFrame")
        fr_link.columnconfigure(0, weight=1)
        fr_link.rowconfigure(0, weight=1)
        fr_link.grid(column=0, row=10, sticky="nsew")

        


    #     # Title Frame Section
    #     # fr_title = ttk.Frame(frame, style="degree_plan_gui.TFrame")
    #     # fr_title.columnconfigure(0, weight=1)
    #     # for r in range(3):
    #     #     fr_title.rowconfigure(r, weight=1)

    #     # lbl_dp = ttk.Label(fr_title, text="Degree Plan Editor", style="GuiTitle.TLabel").grid(column=0, row=0, sticky="n")
    #     # lbl_dp.grid(column=0, row=0, sticky="n")  # text positioning

    #     # # Degree Title Label and design
    #     # lbl_dt = ttk.Label(frame, text="UNIVERSITY OF TEXAS AT DALLAS", style="DegreeTitle.TLabel")
    #     # lbl_dt.grid(column=0, row=1, pady=5)  # text positioning
        


    # #     # Choose student's degree plan track text label and design
    # #     # lbl_dp_track = ttk.Label(frame, text="Choose student's chosen track/Degree Plan:", style="BlSmall.TLabel")
    # #     # lbl_dp_track.grid(column=1, row=1, columnspan=1, padx=5, pady=10)  # text positioning

    # #     # Insert here a Degree Plan Track options list, where the user can add/select/change/remove tracks?

    # #     # Insert here a list of prerequisite courses, where the user can change/delete/add new/add to degree plan?

    # #     # save what track option was selected in a way that the audit report can access it

    # #     # Insert here a way for user to select if the student is doing Fast Track, and save value to student object?

    # #     # Insert here a way for user to select if the student is doing Thesis, and save value to student object?

    # #     # Insert here way for user to generate, update with all info & save where user wants to save student object?

        # Previous Page button and design
        prev_btn = ttk.Button(
            fr_link,
            text="<< Previous",
            command=lambda: self.controller.show_frame("UploadFilePage")
        )
        prev_btn.grid(column=0, row=9, columnspan=1, sticky="sw")  # button positioning

        # Button to direct user to degree_plan_report_page.py in order for user to edit degree plan
        next_btn = ttk.Button(
            fr_link,
            text="Next >>",
            command=lambda: controller.show_frame("DegreePlanReportPage")
        )
        next_btn.grid(column=0, row=9, columnspan=1, sticky="se")  # button padding

    # # note to the developer in charge of the degree plan gui:
    # # This file is just to get, whoever is working on the Degree Plan GUI, a head start on the gui.
    # # there's still the rest of the gui, student object stuff, etc. that you'll need to figure out and add to this
    # # modify it as much as you want to, just make sure to:
    # # include a way for audit_report_page.py to know what degree plan track and prerequisite courses are chosen
