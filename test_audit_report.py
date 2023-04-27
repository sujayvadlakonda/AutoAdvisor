from audit_report import AuditReport
from track import DataScience, IntelligentSystems, Systems


def assertEqual(a, b):
    if not a == b:
        print("A:", a)
        print("B:", b)
        raise Exception("A != B", a, b)


def test_core(audit_report, expected_core):
    assertEqual(audit_report._get_core_identifiers(), expected_core)

def test_electives(audit_report, expected_electives):
    assertEqual(audit_report._get_electives(), expected_electives)

# Notice CS 6320 and 6360 are swapped. Since CS 6320 has the better grade, it should be in core.
ted_lasso = AuditReport("transcripts/ted-lasso.pdf", DataScience())
ted_lasso_core = ["CS 6313", "CS 6350", "CS 6363", "CS 6375", "CS 6320"]
test_core(ted_lasso, ted_lasso_core)
ted_lasso_electives = ["CS 6334", "CS 6349", "CS 6360", "CS 6367", "CS 6382", "SE 6356"]
test_electives(ted_lasso, ted_lasso_electives)

taylor_swift = AuditReport("transcripts/taylor-swift.pdf", DataScience())
taylor_swift_core = ["CS 6313", "CS 6350", "CS 6363", "CS 6375", "CS 6360"]
test_core(taylor_swift, taylor_swift_core)
taylor_swift_electives = ["CS 5343", "CS 6301", "CS 6314", "CS 6320", "CS 6364", "CS 6385"]
test_electives(taylor_swift, taylor_swift_electives)

roy_kent = AuditReport("transcripts/roy-kent.pdf", DataScience())
roy_kent_core = ["CS 6313", "CS 6350", "CS 6363", "CS 6375", "CS 6360"]
test_core(roy_kent, roy_kent_core)
roy_kent_electives = ["CS 5343", "CS 6301", "CS 6314", "CS 6349", "CS 6359", "CS 6367"]
test_electives(roy_kent, roy_kent_electives)

krusty_krab = AuditReport("transcripts/krusty-krab.pdf", DataScience())
krusty_krab_core = ["CS 6313", "CS 6350", "CS 6363", "CS 6375", "CS 6360"]
test_core(krusty_krab, krusty_krab_core)
krusty_krab_electives = ["CS 5343", "CS 6301", "CS 6314", "CS 6323", "CS 6334", "CS 6385"]
test_electives(krusty_krab, krusty_krab_electives)

monica_geller = AuditReport("transcripts/monica-geller.pdf", DataScience())
monica_geller_core = ["CS 6313", "CS 6350", "CS 6363", "CS 6375", "CS 6360"]
test_core(monica_geller, monica_geller_core)
monica_geller_electives = ["CS 5343", "CS 6314", "CS 6349", "CS 6359", "CS 6367", "CS 6396"]
test_electives(monica_geller, monica_geller_electives)

mike_modano = AuditReport("transcripts/mike-modano.pdf", IntelligentSystems())
mike_modano_core = ["CS 6320", "CS 6363", "CS 6364", "CS 6375", "CS 6360"]
test_core(mike_modano, mike_modano_core)
mike_modano_electives = ["CS 5343", "CS 6301", "CS 6314", "CS 6322", "CS 6356", "CS 6359"]
test_electives(mike_modano, mike_modano_electives)

stevie_budd = AuditReport("transcripts/stevie-budd.pdf", IntelligentSystems())
stevie_budd_core = ["CS 6320", "CS 6363", "CS 6364", "CS 6375", "CS 6360"]
test_core(stevie_budd, stevie_budd_core)
stevie_budd_electives = ["CS 5343", "CS 6301", "CS 6314", "CS 6322", "CS 6385", "CS 6396"]
test_electives(stevie_budd, stevie_budd_electives)

# Chandler never took CS 6352, only CS 6350
chandler_bing = AuditReport("transcripts/chandler-bing.pdf", Systems())
chandler_bing_core = ["CS 6304", "CS 6363", "CS 6378", "CS 6396", "CS 6380"]
test_core(chandler_bing, chandler_bing_core)
chandler_bing_electives = ["CS 5343", "CS 6314", "CS 6324", "CS 6352", "CS 6360", "CS 6385"]
test_electives(chandler_bing, chandler_bing_electives)
