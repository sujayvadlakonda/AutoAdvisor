from audit_report import AuditReport
from track import DataScience, IntelligentSystems, Systems


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

taylor_swift = AuditReport("transcripts/taylor-swift.pdf", DataScience())
taylor_swift_core = ["CS 6313", "CS 6350", "CS 6363", "CS 6375", "CS 6360"]
test_core(taylor_swift, taylor_swift_core)

roy_kent = AuditReport("transcripts/roy-kent.pdf", DataScience())
roy_kent_core = ["CS 6313", "CS 6350", "CS 6363", "CS 6375", "CS 6360"]
test_core(roy_kent, roy_kent_core)

krusty_krab = AuditReport("transcripts/krusty-krab.pdf", DataScience())
krusty_krab_core = ["CS 6313", "CS 6350", "CS 6363", "CS 6375", "CS 6360"]
test_core(krusty_krab, krusty_krab_core)

monica_geller = AuditReport("transcripts/monica-geller.pdf", DataScience())
monica_geller_core = ["CS 6313", "CS 6350", "CS 6363", "CS 6375", "CS 6360"]
test_core(monica_geller, monica_geller_core)

mike_modano = AuditReport("transcripts/mike-modano.pdf", IntelligentSystems())
mike_modano_core = ["CS 6320", "CS 6363", "CS 6364", "CS 6375", "CS 6360"]
test_core(mike_modano, mike_modano_core)

stevie_budd = AuditReport("transcripts/stevie-budd.pdf", IntelligentSystems())
stevie_budd_core = ["CS 6320", "CS 6363", "CS 6364", "CS 6375", "CS 6360"]
test_core(stevie_budd, stevie_budd_core)

chandler_bing = AuditReport("transcripts/chandler-bing.pdf", Systems())
chandler_bing_core = ["CS 6304", "CS 6363", "CS 6378", "CS 6396", "CS 6380"]
test_core(chandler_bing, chandler_bing_core)
