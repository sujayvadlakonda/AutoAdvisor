from audit_report import AuditReport
from track import DataScience, IntelligentSystems, Systems, Traditional, InteractiveComputing, SoftwareEngineering


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
ted_lasso_electives = ["CS 6334", "CS 6349", "CS 6360", "CS 6367", "CS 6382", "SE 6356"]

taylor_swift = AuditReport("transcripts/taylor-swift.pdf", DataScience())
taylor_swift_core = ["CS 6313", "CS 6350", "CS 6363", "CS 6375", "CS 6360"]
taylor_swift_electives = ["CS 5343", "CS 6301", "CS 6314", "CS 6320", "CS 6364", "CS 6385"]

roy_kent = AuditReport("transcripts/roy-kent.pdf", DataScience())
roy_kent_core = ["CS 6313", "CS 6350", "CS 6363", "CS 6375", "CS 6360"]
roy_kent_electives = ["CS 5343", "CS 6301", "CS 6314", "CS 6349", "CS 6359", "CS 6367"]

krusty_krab = AuditReport("transcripts/krusty-krab.pdf", DataScience())
krusty_krab_core = ["CS 6313", "CS 6350", "CS 6363", "CS 6375", "CS 6360"]
krusty_krab_electives = ["CS 5343", "CS 6301", "CS 6314", "CS 6323", "CS 6334", "CS 6385"]

monica_geller = AuditReport("transcripts/monica-geller.pdf", DataScience())
monica_geller_core = ["CS 6313", "CS 6350", "CS 6363", "CS 6375", "CS 6360"]
monica_geller_electives = ["CS 5343", "CS 6314", "CS 6349", "CS 6359", "CS 6367", "CS 6396"]

mike_modano = AuditReport("transcripts/mike-modano.pdf", IntelligentSystems())
mike_modano_core = ["CS 6320", "CS 6363", "CS 6364", "CS 6375", "CS 6360"]
mike_modano_electives = ["CS 5343", "CS 6301", "CS 6314", "CS 6322", "CS 6356", "CS 6359"]

stevie_budd = AuditReport("transcripts/stevie-budd.pdf", IntelligentSystems())
stevie_budd_core = ["CS 6320", "CS 6363", "CS 6364", "CS 6375", "CS 6360"]
stevie_budd_electives = ["CS 5343", "CS 6301", "CS 6314", "CS 6322", "CS 6385", "CS 6396"]

keeley_jones = AuditReport("transcripts/keeley-jones.pdf", IntelligentSystems())
keeley_jones_core = ["CS 6320", "CS 6363", "CS 6364", "CS 6375", "CS 6360"]
keeley_jones_electives = ["CS 6301", "CS 6313", "CS 6332", "CS 6359", "CS 6371", "CS 6380"]

# Chandler never took CS 6352, only CS 6350
chandler_bing = AuditReport("transcripts/chandler-bing.pdf", Systems())
chandler_bing_core = ["CS 6304", "CS 6363", "CS 6378", "CS 6396", "CS 6380"]
chandler_bing_electives = ["CS 5343", "CS 6314", "CS 6324", "CS 6350", "CS 6360", "CS 6385"]

harry_potter = AuditReport("transcripts/harry-potter.pdf", Traditional())
harry_potter_core = ["CS 6363", "CS 6378", "CS 6390", "CS 6353", "CS 6360"]
harry_potter_electives = ["CS 5343", "CS 6314", "CS 6326", "CS 6359", "CS 6380", "CS 6396"]

# Ron had his 5xxx elective at the end, but this differs from how other audit reports are
ron_weasley = AuditReport("transcripts/ron-weasley.pdf", Traditional())
ron_weasley_core = ["CS 6363", "CS 6378", "CS 6390", "CS 6353", "CS 6360"]
ron_weasley_electives = ["CS 5333", "CS 6314", "CS 6350", "CS 6359", "CS 6364", "CS 6385"]

jaime_tartt = AuditReport("transcripts/jaime-tartt.pdf", InteractiveComputing())
jaime_tartt_core = ["CS 6326", "CS 6363", "CS 6323", "CS 6334", "CS 6366"]
jaime_tartt_electives = ["CS 6301", "CS 6313", "CS 6319", "CS 6360", "CS 6375", "CS 6384"]

rachel = AuditReport("transcripts/rachel-green.pdf", SoftwareEngineering())
rachel_core = ["SE 6329", "CS 6361", "SE 6362", "SE 6367", "SE 6387"]
rachel_elec = ["CS 6320", "CS 6324", "CS 6350", "CS 6360", "CS 6363", "CS 6375"]

test_core(ted_lasso, ted_lasso_core)
test_core(taylor_swift, taylor_swift_core)
test_core(roy_kent, roy_kent_core)
test_core(krusty_krab, krusty_krab_core)
test_core(monica_geller, monica_geller_core)
test_core(mike_modano, mike_modano_core)
test_core(stevie_budd, stevie_budd_core)
test_core(keeley_jones, keeley_jones_core)
test_core(chandler_bing, chandler_bing_core)
test_core(harry_potter, harry_potter_core)
test_core(ron_weasley, ron_weasley_core)
test_core(jaime_tartt, jaime_tartt_core)
test_core(rachel, rachel_core)

test_electives(ted_lasso, ted_lasso_electives)
test_electives(taylor_swift, taylor_swift_electives)
test_electives(roy_kent, roy_kent_electives)
test_electives(krusty_krab, krusty_krab_electives)
test_electives(monica_geller, monica_geller_electives)
test_electives(mike_modano, mike_modano_electives)
test_electives(stevie_budd, stevie_budd_electives)
test_electives(keeley_jones, keeley_jones_electives)
test_electives(chandler_bing, chandler_bing_electives)
test_electives(harry_potter, harry_potter_electives)
test_electives(ron_weasley, ron_weasley_electives)
test_electives(jaime_tartt, jaime_tartt_electives)
test_electives(rachel, rachel_elec)


audit_report = AuditReport("transcripts/monica-geller.pdf", DataScience())
print(audit_report.get_remaining_elec_courses())
