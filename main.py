from degreeApp import DegreeApp
# from uploadFile import UploadFilePage

if __name__ == '__main__':
    app = DegreeApp()  # application window instance

    # leo, did you mean something like this?
    # files = UploadFilePage()
    # filepath = files.get_filepath()
    # pass file path to sujay's code somewhere here?

    app.mainloop()  # keeps window running until exited


# personal side notes that I'll delete later:
# adding "file_path = file_selection()" in file_select_gui() causes file explorer to open before the button is clicked
# adding "return file_path" in file_selection() causes file explorer to open before the button is clicked
# don't put () after button commands or the button will activate before you press it
# if picture doesn't show up in uploadFile.py then swap out the decorative image label code with:
# self.doc_upload_photo = tk.PhotoImage(file=r"./images/upload_file.png")
#        self.lbl_image = ttk.Label(
#            frame,
#            image=self.doc_upload_photo,
#            style="picBkgd.TLabel"
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
# if want classB(vari of vari = classA()) in main, then in classB.py: use def init(self, container) & super().__init__(container)
# (under def __init__(self) function) def initUI(self): self.master.title("windowTitle"), self.pack(fill=BOTH)
# the self.master makes variable known to root tk() window
# when passing ttk.Frame to classB(ttk.Frame), the self. is assigning widgets to ttk.Frame, so req assign frame to the root window with self.grid(row=0, column=0) or self.pack(fill="both", expand=True) in def innit function
# initUI(self) is e.g.'s example function used to call to make window ui since class ClassName(Frame)
# super() for inherit methods+properties from another class
# in def init(), to set up variables can do with self or without self.variableName = passedParameter/chosenValue
# assign widgets+style as self.variableName underneath super().__init__(Frame)
# replace window variable in the labels () etc. with self, but keep frame variable
# pass self as a function parameter
# call function with parameters: don't include self. parameter, but add self. to begining of function call
# can assign variable name to self. object to be able to reference them in other class methods
# any variable that has self. attached to it must have self. when used in other locations
# add self. to self.widgetName = ttk.widgetName, but not the right side ttk.widgetName
# calling function in same class: className.functionName(self)
# add self.buttonName['command'] = self.FunctionName as long as function name is in the same class
# in classB file, to call function you do self.functionName() inside def __innit__(self) function
# textvariable in label: est self.variName = tk.StringVar() in def innit() function, sep self. vari for labelVari and textvariable vari,
# to change textvariable vari: self.textvariableVari.set(newValue)
# Add to the top of the degreeApp.py file: from insertYourFileNameHere import insertYourClassNameHere
# In the degreeApp.py file, add your file's class name to the () in the For Loop
# In the prev/next button's command section, make sure the class name is enclosed in ""


# pulled out constants
# ask where they store the name of the track so that I could add it to audit report
# ask if they're storing pre-req in json file so that I can access it
# ck if leo is able to call the file path just fine

# window = tk.Tk()  # makes a tkinter frame instance (from degreeApp.py)
# from tkinter.messagebox import showinfo, showinfo(title="Uploaded File",message=file_name)
# self.file_select_gui(), def file_select_gui(self):
# self.pack(fill=BOTH, expand=True)  # assigns ttk.Frame to root application window. get rid of this
# self.style.configure("switchPage.TButton", font=("Segoe UI", 14), foreground="black", background="#800080")
# style="switchPage.TButton",
# frame.pack(fill=BOTH, expand=False)  # frame padding
# lbl_image.pack(side=TOP, fill=NONE, padx=(20, 0), pady=(5, 0))  # padding
# lbl_upload.pack(fill=NONE, expand=False, padx=30)  # text padding
# lbl_upload_instruct.pack(fill=NONE, expand=False, padx=20, pady=(10, 0))  # text padding
# btn_file_browse.pack(side=TOP, pady=(15, 0))  # button padding
# self.file_name.pack(pady=(10, 0))
# prev_btn.pack(pady=(5, 20))  # button padding
# next_btn.pack(pady=(5, 20))  # button padding
# self.container = container
# self.container.grid(column=0, row=0, sticky="nsew")
# self.container.grid_columnconfigure(0, weight=1)
# self.container.grid_rowconfigure(0, weight=1)
# if you want a column to be uniform width: columnconfigure include: uniform
#  Segoe UI/print, bookman old style, bradley hand ITC/ink free, candara light, century gothic
#  003300, 003333, 006600, 006633, 086623, 3DA542 (green),
#  107896, 1287A8, 43ABC9, #4582ec, 0032A0, 1496BB, 0247fe, 2B0080 (button opt), 394C7F (blue),
#  #593196, 7442C8, 800080, 575068 (purple), 5901c0, 8601af, 800080, 33058d, 6610F2, 6610f2, #553980
#  light blue: #ACC8E5, #A1FCFF, #E3FFFF, A6F4FF
# .grid(): rowspan, ipadx, ipady
