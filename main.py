from degreeApp import DegreeApp
from uploadFile import UploadFile


if __name__ == '__main__':
    app = DegreeApp()  # application window instance
    UploadFile(app)  # passes application window object to Upload File class
    app.mainloop()  # keeps window running until exited
