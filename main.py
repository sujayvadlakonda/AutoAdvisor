from degreeApp import DegreeApp
# from uploadFile import UploadFilePage

if __name__ == '__main__':
    app = DegreeApp()  # application window instance

    # leo did you mean something like this?
    # files = UploadFilePage()
    # filepath = files.get_filepath()
    # pass file path to sujay's code?

    app.mainloop()  # keeps window running until exited
