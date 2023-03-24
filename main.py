from degreeApp import DegreeApp
from uploadFile import UploadFile
# from homepage import Homepage

if __name__ == '__main__':
    app = DegreeApp()  # application window instance
    UploadFile(app)  # passes application window object to Upload File class
    app.mainloop()  # keeps window running until exited


# personal side notes that I'll delete later:
# adding "file_path = file_selection()" in file_select_gui() causes file explorer to open before the button is clicked
# adding "return file_path" in file_selection() causes file explorer to open before the button is clicked
# don't put () after button commands or the button will activate before you press it
# labelName["text"] = filename # changes parameter without needing config after value already set
# current_theme = style.theme_use("vista"), vista/default
#  from fileName import ClassName
# chosenVariableName = className(), chosenVariableName.functionInClassName() used to call method in class
# if don't do super then classB(classAName):
# if want classB(vari of vari = classA()) in main, then in classB.py, def init(self, container) & super().__init__(container)
# (under def __init__(self) function) def initUI(self): self.master.title("windowTitle"), self.pack(fill=BOTH)
# the self.master makes variable known to root tk() window
# when passing ttk.Frame to classB(ttk.Frame), the self. is assigning widgets to ttk.Frame, so req assign frame to the root window with self.grid(row=0, column=0) or self.pack(fill="both", expand=True) in def innit function
# initUI(self) is e.g.'s example function used to call to make window ui since class ClassName(Frame)
# super() for inherit methods+properties from another class
# in def init(), to set up variables can do with self or without self.variableName = passedParameter/chosenValue
# assign widgets+style as self.variableName underneath super().__init__(Frame)
# replace window variable in the labels () etc. with self, but keep frame variable
# pass self as a a function parameter
# can assign variable name to self. object to be able to reference them in other class methods
# any variable that has self. attached to it must have self. when used in other locations
# add self. to self.widgetName = ttk.widgetName, but not the right side ttk.widgetName
# calling function in same class: className.functionName(self)
# add self.buttonName['command'] = self.FunctionName as long as function name is in the same class
# in classB file, to call function you do self.functionName() inside def __innit__(self) function
# textvariable in label: est self.variName = tk.StringVar() in def innit() function, sep self. vari for labelVari and textvariable vari,
# to change textvariable vari: self.textvariableVari.set(newValue)


#  other page sep class and files
#  pulled-out constants
#  do we include self.master.title?
#  add a prev + next button that goes to next window page that looks nice
#  add nice homepage w/ degree plan and audit tool label, and "+ Start" button, that goes to upload file page

# window = tk.Tk()  # makes a tkinter frame instance
# showinfo(
#                 title="Uploaded File",
#                 message=file_name
#             )
