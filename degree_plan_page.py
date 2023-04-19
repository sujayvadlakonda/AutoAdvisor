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
        
        style.configure("big_heading.TLabel", font=("Segoe print", 30, "bold"), foreground="black", background="orange")
        style.configure("medium_heading.TLabel", font=("Verdana", 25), foreground="black", background="orange")
        style.configure("bold_heading.TLabel", font=("Segoe print", 25, "bold"), foreground="black", background="orange")

        style.configure("normal_text.TLabel", font=("Bookman Old Style", 14), foreground="black", background="orange")
        style.configure("filling_text.TLabel", font=("Bookman Old Style", 14), foreground="black", background="white", relief="sunken")
        style.configure("course_section.TLabel", font=("Bookman Old Style", 14), foreground="orange", background="black")

        style.configure("TRadiobutton", font=("Bookman Old Style", 14), foreground="black", background="orange", relief="flat")
    
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
        lbl_gui.grid(column=0, row=0, pady=5)  # text positioning

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
        lbl_title.grid(column=0, row=0, pady=(10,5))
        lbl_title = ttk.Label(fr_title, text="UNIVERSITY OF TEXAS AT DALLAS", style="medium_heading.TLabel")
        lbl_title.grid(column=0, row=1)
        lbl_title = ttk.Label(fr_title, text="MASTER OF COMPUTER SCIENCE", style="medium_heading.TLabel")
        lbl_title.grid(column=0, row=2)

        # Get and Display Student's Major
        lbl_major = ttk.Label(fr_title, text=std_major, style="bold_heading.TLabel")
        lbl_major.grid(column=0, row=4, pady=(0,10))
       
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
        lbl_student.grid(column=0, row=0, sticky='w', padx=5, pady=(10,5))

        lbl_student = ttk.Label(fr_student, text=std_name, style="filling_text.TLabel")
        lbl_student.grid(column=1, row=0, sticky='w', padx=5, pady=5)

        # Student ID
        lbl_student = ttk.Label(fr_student, text="Student ID Number:", style="normal_text.TLabel")
        lbl_student.grid(column=0, row=1, sticky='w', padx=5, pady=5)
   
        lbl_student = ttk.Label(fr_student, text=std_id, style="filling_text.TLabel")
        lbl_student.grid(column=1, row=1, sticky='w', padx=5, pady=5)

        # Semester Additted
        lbl_student = ttk.Label(fr_student, text="Semester Admitted \n to Program:", style="normal_text.TLabel")
        lbl_student.grid(column=0, row=2, sticky='w', padx=5, pady=(5,10))
   
        lbl_student = ttk.Label(fr_student, text=std_sem_admitted, style="filling_text.TLabel")
        lbl_student.grid(column=1, row=2, sticky='w', padx=5, pady=5)
 
        # FT, Thesis, Anticipated
        def yes_no(c_index, r_index):
            selected_value = tk.StringVar()
            options = (   ('Yes', 'Y'),
                    ('No', 'N'))
            for opt in options:
                r = ttk.Radiobutton(                        
                                fr_student,
                                text=opt[0],
                                value=opt[1],
                                variable=selected_value,
                                style="TRadiobutton"
                )
                r.grid(column=c_index, row=r_index, sticky='w', padx=(10,0))
                c_index += 1

        # Fast Track
        lbl_student = ttk.Label(fr_student, text="FT:", style="normal_text.TLabel")
        lbl_student.grid(column=2, row=0, sticky='w', padx=5, pady=5)
        yes_no(3, 0)  # (column, row)

        # Thesis
        lbl_student = ttk.Label(fr_student, text="Thesis:", style="normal_text.TLabel")
        lbl_student.grid(column=2, row=1, sticky='w', padx=5, pady=5)
        yes_no(3, 1)

        # Anticipated Graduation
# need to save this info somewhere for Degree Plan Report Later
        lbl_student = ttk.Label(fr_student, text="Anticipated \n Graduation", style="normal_text.TLabel")
        lbl_student.grid(column=2, row=2, sticky='w', padx=5, pady=5)

        expect_grad = tk.StringVar()      
        entry_student = ttk.Entry(fr_student, text=expect_grad, font=("Bookman Old Style", 14), foreground="black")
        entry_student.grid(column=3, row=2, sticky='w', columnspan=2)      

# 3. Note, Advisor, Date Frame
        c3=4
        r3=4
        fr_note = ttk.Frame(frame, style="section.TFrame")
        for c in range(c3):
            fr_note.columnconfigure(c, weight=1)
        for r in range(r3):
            fr_note.rowconfigure(r, weight=1)
        fr_note.grid(column=0, row=3, sticky="nsew", pady=5)

         # Labeling note
# Should i hard code note or get info depend on which major.
# Need to talk to Aleky and Aiden about it
        lbl_note= ttk.Label(fr_note, text="* May include any 6000 or 7000 level CS course with prior permission", style="normal_text.TLabel")
        lbl_note.grid(column=0, row=1, columnspan=4, pady=(10,20))

        # Labeling Academic Advisor
        lbl_note = ttk.Label(fr_note, text="Academic Advisor", style="normal_text.TLabel")
        lbl_note.grid(column=0, row=3, sticky='w', padx=(5,0), pady=(5,10))

        advisor_name = tk.StringVar()      
        entry_note = ttk.Entry(fr_note, text=advisor_name, font=("Bookman Old Style", 14), foreground="black")
        entry_note.grid(column=1, row=3, sticky='w', padx=5, pady=5)

        # Labeling Date
        lbl_note = ttk.Label(fr_note, text="Date Submitted", style="normal_text.TLabel")
        lbl_note.grid(column=2, row=3, sticky='e', padx=(0,5), pady=5)

        advisor_name = tk.StringVar()      
        entry_note = ttk.Entry(fr_note, text=advisor_name, font=("Bookman Old Style", 14), foreground="black")
        entry_note.grid(column=3, row=3, sticky='e', padx=5, pady=5)

# 4. Linkup Frame
        # fr_link= ttk.Frame(frame, style="section.TFrame")
        # fr_link.columnconfigure(0, weight=1)
        # fr_link.rowconfigure(0, weight=1)
        # fr_link.grid(column=0, row=4, sticky="nsew", pady=5)  

        c_link=2
        r_link=1
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
        prev_btn.grid(column=0, row=0, sticky='w', padx=(10,5), pady=10)  # button positioning

        # Go to Homepage Button
        homepage_btn = ttk.Button(
            fr_link,
            text="Go to Homepage",
            command=lambda: self.controller.show_frame("HomepageStart")
        )
        homepage_btn.grid(column=0, row=0, padx=5, pady=10)  # button positioning
        
        # Launch PDF Button
        launch_pdf_btn = ttk.Button(
            fr_link,
            text="Launch PDF Editor",
            # command=lambda: controller.show_frame("DegreePlanReportPage")
        )
        launch_pdf_btn.grid(column=1, row=0, padx=5, pady=10)  # button positioning
        
        # Button to direct user to degree_plan_report_page.py in order for user to edit degree plan
        next_btn = ttk.Button(
            fr_link,
            text="Next >>",
            command=lambda: controller.show_frame("DegreePlanReportPage")
        )
        next_btn.grid(column=1, row=0, sticky="e", padx=(0,10), pady=10)  # button padding

       