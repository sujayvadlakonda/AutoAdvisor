from degreeApp import DegreeApp
from transcript import *
# from uploadFile import UploadFilePage

if __name__ == '__main__':
    app = DegreeApp()  # application window instance

    # leo did you mean something like this?
    # files = UploadFilePage()
    # filepath = files.get_filepath()
    # pass file path to sujay's code?

    ted_lasso = Transcript("transcripts/ted-lasso.pdf")
    name = ted_lasso.get_name()
    id = ted_lasso.get_id()
    major = ted_lasso.get_major()
    semester = ted_lasso.get_beginning_of_graduate_record()
    print(name, id, major, semester)
    ted_lasso.course_finder()



    app.mainloop()  # keeps window running until exited
