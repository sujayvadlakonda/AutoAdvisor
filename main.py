from degreeApp import DegreeApp
from uploadFile import UploadFilePage
from homepage import HomepageStart
from degreePlan import DegreePlanPage
from auditReport import AuditReportPage
from transcript import *
# from uploadFile import UploadFilePage

if __name__ == '__main__':
    app = DegreeApp()  # application window instance

    # leo did you mean something like this?
    # files = UploadFilePage()
    # filepath = files.get_filepath()
    # pass file path to sujay's code?

    files = UploadFilePage()
    filepath = files.get_filepath()
    # selected_file = Transcript(filepath)

    # selected_file = Transcript("transcripts/ted-lasso.pdf")
    # name = selected_file.get_name()
    # id = selected_file.get_id()
    # major = selected_file.get_major()
    # semester = selected_file.get_beginning_of_graduate_record()
    # print(name, id, major, semester)
    # selected_file.course_finder()




    app.mainloop()  # keeps window running until exited
