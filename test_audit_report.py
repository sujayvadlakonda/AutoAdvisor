import unittest

from course_finder import get_courses
from audit_report import AuditReport, DataScience

class TestAuditReport(unittest.TestCase):
    def test_ted_lasso(self):
        courses = get_courses("transcripts/ted-lasso.pdf")
        requirements = DataScience()
        audit_report = AuditReport(courses, requirements)
        core_fulfilled = audit_report.get_requirements_fulfilled()
        expected = ["CS 6363", "CS 6313", "CS 6350", "CS 6375"]
        self.assertEqual(core_fulfilled, expected)



unittest.main()
