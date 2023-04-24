from degree_app import DegreeApp


if __name__ == '__main__':
    app = DegreeApp()  # application window instance

    app.mainloop()  # keeps window running until exited


# personal side notes that I'll delete later:
# window = tk.Tk()  # makes a tkinter frame instance
# adding "file_path = file_selection()" in file_select_gui() causes file explorer to open before the button is clicked
# adding "return file_path" in file_selection() causes file explorer to open before the button is clicked
# don't put () after button commands or the button will activate before you press it
# if picture doesn't show up in upload_file_page.py then swap out the decorative image label code with:
# self.doc_upload_photo = tk.PhotoImage(file=r"./images/upload_file.png")
#        self.lbl_image = ttk.Label(
#            frame,
#            image=self.doc_upload_photo,
#            style="pic_background.TLabel"
#        )
#        self.lbl_image.doc_upload_photo = self.doc_upload_photo  # image reference needed to display image w/o self.
#        self.lbl_image.pack(side=TOP, fill=NONE, expand=5, padx=(20, 0), pady=(20, 10))  # padding
# however, if you get rid of the self for images then you need to reference the image
# labelName["text"] = filename # changes parameter without needing config after value already set
# to pass parameter to button command format it as command = lambda : functionName(parameterName)
# current_theme = style.theme_use("vista"), vista/default
#  from fileName import ClassName
# chosenVariableName = className(), chosenVariableName.functionInClassName() used to call method in class
# if you don't do use super, then classB(classAName):
# if add classB(vari of vari = classA()) in main, then classB.py: def init(self, container) & super().init(container)
# (under def __init__(self) function) def initUI(self): self.master.title("windowTitle"), self.pack(fill=BOTH)
# the self.master makes variable known to root tk() window
# classB(ttk.Frame): self. assign widget to ttk.Frame, so assign frame to root win w/ def innit() self.grid(row=0, column=0)
# initUI(self) is e.g.'s example function used to call to make window ui since class ClassName(Frame)
# super() for inherit methods+properties from another class
# in def init(), to set up variables can do with self or without self.variableName = passedParameter/chosenValue
# assign widgets+style as self.variableName underneath super().__init__(Frame)
# replace window variable in the labels () etc. with self, but keep frame variable
# pass self as a function parameter
# call function with parameters: don't include self. parameter, but add self. to beginning of function call
# can assign variable name to self. object to be able to reference them in other class methods
# any variable that has self. attached to it must have self. when used in other locations
# add self. to self.widgetName = ttk.widgetName, but not the right side ttk.widgetName
# calling function in same class: className.functionName(self)
# add self.buttonName['command'] = self.FunctionName as long as function name is in the same class
# in classB file, to call function you do self.functionName() inside def __innit__(self) function
# label's text variable: self.variName = tk.StringVar() in def innit() function, self.vari for labelVari & text variable
# to change text variable: self.textVariable.set(newValue)
# run a file other than my own: edit run configurations, to have script path be the file you want to run
# mac: can't use filetypes (mac doesn't have file type dropdown menu), but can use initialdir = "/"
# from tkinter.messagebox import showinfo, showinfo(title="Saved File",message="File Saved)
# if you want a column to be uniform width: columnconfigure include: uniform
# radio button: add command for it to save value, num val in num order otherwise it pre-selects the smaller num for you
# dict = {"x": [], "y": []}
# dict["a"].append(listOne)
# len(dp_pre_req_class) # length of list
# self.disp_selections[course_counter] = disp_select_one # aka  disp_select_one in option menu for dict
# ListVariName.insert(indexNum, 'Word')
# page navigation button to work:
# Add to the top of the degree_app.py file: from insertYourFileNameHere import insertYourClassNameHere
# In the degree_app.py file, add your file's class name to the () in the For Loop
# In the button's command section, make sure the class name is enclosed in ""
# Font: Segoe UI, bookman old style, bradley hand ITC/ink free, candara light, century gothic
# green: 003300, 003333, 006600, 006633, 086623, 3DA542
# blue: 107896, 1287A8, 43ABC9, #4582ec, 0032A0, 1496BB, 0247fe, 2B0080, 394C7F, 97DFFC
# purple: #593196, 7442C8, 800080, 575068, 5901c0, 8601af, 800080, 33058d, 6610F2, 6610f2, #553980
# light blue: ACC8E5, A1FCFF, E3FFFF, A6F4FF, 89cff0, 87ceeb (bg), b0e0e6
# gray: #f5f5f5, #d3d3d3,
# off white: f8f8ff (bg)
# tk.StringVar(container, value), name_var.get() for same file StringVar() stuff
# print(self.disposition_dict["disp_options"][0])
# def print_core(self) from class AuditReport in audit_report.py (the one that has core = self._get_core_identifiers()
# make sure document.save is list
# font.size = Pt(12)
# doc_styles["Normal"}
# paragraph = document.add_paragraph('A plain paragraph having some ', style="Normal"))
# paragraph.style = "Normal"
# bold at start need sep run from non bolded text and the 1st run needs a space at the end
# run = paragraph.add_run('dolor')
# run.bold = True
# paragraph = document.add_paragraph('Normal text, ')
# paragraph.add_run('text with emphasis.', 'Emphasis')
# run = paragraph.add_run('text with emphasis.')
# run.style = 'Emphasis'
# from docx.text.run import Font
# body_style = document.styles["Body Text"]
# report_style = document.styles["Normal"]
# fonts = report_style.font
# fonts.name = "Calibri"  # sets default font
# format_ar_title.name = "Calibri"  # sets font
# requirements that akelanda would follow for their part of the code:
#   If GPA needed in remaining course(s) is >= 2.00:
#   then, if one course remaining display: The student needs >= C+, B-, etc. in CS xxxx
#   or if multiple courses remaining display: The student needs a GPA >= x.xx in: CS xxxx, CS xxxx, etc.
#   If GPA needed in remaining course(s) is < 2.00: Display: The student must pass CS xxxx, CS xxxx, etc.
#   or if the course completed then e.g. Core Complete.
#   To graduate the student must have a Core GPA >= 3.19.
#   or to graduate with a 3.0 <= Core GPA < 3.19 if they complete an extra 6000+ level CS/SE course.
#   To graduate the student must have an overall + elective GPA >= 3.00.

# have gpa section and courses display on gui, word doc generation w/ sem of completion,
# add the latest code from gitHub
# figure out why uncommenting the import audit report causes text to print out on terminal
