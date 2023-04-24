from audit_report import AuditReport
from track import DataScience


def assertEqual(a, b):
    if not a == b:
        print("A:", a)
        print("B:", b)
        raise Exception("A != B", a, b)


def test_core(audit_report, expected_core):
    assertEqual(audit_report._get_core_identifiers(), expected_core)


ted_lasso = AuditReport("transcripts/ted-lasso.pdf", DataScience())
ted_lasso_core = ["CS 6313", "CS 6350", "CS 6363", "CS 6375", "CS 6320"]
test_core(ted_lasso, ted_lasso_core)
