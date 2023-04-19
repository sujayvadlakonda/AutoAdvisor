from transcript import Transcript
from course import Courses
from track import DataScience
from audit_report import AuditReport

transcript = Transcript("transcripts/ted-lasso.pdf")
courses = transcript.get_courses()
courses = Courses(courses)
track = DataScience()
audit_report = AuditReport(transcript, track)
audit_report.print_courses()
