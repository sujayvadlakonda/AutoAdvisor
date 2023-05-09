from course_finder import get_courses

letter_grade_points = {
                    "A ": 4.000,
                    "A- ": 3.670,
                    "B+ ": 3.330,
                    "B ": 3.000,
                    "B- ": 2.670,
                    "C+ ": 2.330,
                    "C ": 2.000,
                    "F ": 0.000,
                    "P ": 0.000,
                    "W ": 0.000
                }


class AuditReport:
    def __init__(self, path_to_transcript, track):
        courses = get_courses(path_to_transcript)
        self.courses = courses
        self.track = track

    def get_gpas_section(self):
        gpas_section = ""
        gpas_section += self.get_core_gpa_section() + "\n"
        gpas_section += self.get_elective_gpa_section() + "\n"
        gpas_section += self.get_combined_gpa_section() + "\n"
        return gpas_section

    def get_core_gpa_section(self):
        core_gpa_section = ""
        core_gpa = str(self.get_core_gpa())
        core_gpa_section += core_gpa
        return core_gpa_section

    def get_elective_gpa_section(self):
        elec_gpa_section = ""
        elec_gpa = str(self.get_elec_gpa())
        elec_gpa_section += elec_gpa
        return elec_gpa_section

    def get_combined_gpa_section(self):
        combined_gpa_section = ""
        combined_gpa = str(self.get_combined_gpa())
        combined_gpa_section += combined_gpa
        return combined_gpa_section

    def get_courses_section(self):
        courses_section = ""
        courses_section += self.get_core_section() + "\n"
        courses_section += self.get_electives_section() + "\n\n"
        courses_section += self.get_leveling_section() + "\n"
        return courses_section

    def get_core_section(self):
        core_section = ""
        core = self._get_core_identifiers()
        core = ", ".join(core)
        core_section += core
        return core_section

    def get_electives_section(self):
        electives_section = ""
        ids = self._get_electives()
        ids = ", ".join(ids)
        electives_section += ids
        return electives_section

    def get_leveling_section(self):
        leveling_section = ""

        for leveling in self.track.leveling_courses:
            leveling_section += leveling.to_string(self.courses) + "\n"

        return leveling_section

    def get_outstanding_requirements_section(self):
        outstanding_requirements_section = ""
        outstanding_requirements_section += str(self.get_outstanding_core_gpa()) + "\n"
        outstanding_requirements_section += str(self.get_outstanding_elec_gpa()) + "\n"
        outstanding_requirements_section += str(self.get_outstanding_overall_gpa()) + "\n"
        print(outstanding_requirements_section)
        return outstanding_requirements_section

    # Returns core courses on transcript regardless of completion status
    def _get_core_identifiers(self):
        core_courses = []

        for requirement in self.track.core_requirements:
            requirement_courses = requirement.is_met(self.courses)
            if requirement_courses:
                if not isinstance(requirement_courses, list):
                    requirement_courses = [requirement_courses]
                for requirement_course in requirement_courses:
                    identifier = requirement_course["course_id"]
                    core_courses.append(identifier)

        return core_courses

    def _get_electives(self):
        electives = self.track.get_electives(self.courses)

        ids = []
        for elective in electives:
            id = elective["course_id"]
            grade = elective["grade"]
            credits_earned = elective["earned"]

            if not credits_earned == 0 or grade is None:
                ids.append(id)

        ids.sort()
        return ids

    def letter_grade_needed(self, needed_gpa):

        needed_grade = "C+"

        if (needed_gpa > 3.670):
            needed_grade = "A"
        elif (needed_gpa > 3.330):
            needed_grade = "A-"
        elif (needed_gpa > 3.000):
            needed_grade = "B+"
        elif (needed_gpa > 2.670):
            needed_grade = "B"
        elif (needed_gpa > 2.330):
            needed_grade = "B-"

        return needed_grade

    # To get all remaining (uncompleted) core courses
    def get_remaining_core_courses(self):
        remaining_core_courses = []

        for requirement in self.track.core_requirements:
            requirement_courses = requirement.is_met(self.courses)
            if requirement_courses:
                if not isinstance(requirement_courses, list):
                    requirement_courses = [requirement_courses]
                for requirement_course in requirement_courses:
                    id = requirement_course["course_id"]
                    letter_grade = requirement_course["grade"]

                if (letter_grade is None):
                    remaining_core_courses.append(id)

        remaining = remaining_core_courses
        remaining = ", ".join(remaining)

        return remaining_core_courses

    # To get all remaining (uncompleted) elective courses
    def get_remaining_elec_courses(self):
        remaining_elec_courses = []

        electives = self.track.get_electives(self.courses)

        for elective in electives:
            id = elective["course_id"]
            letter_grade = elective["grade"]
            credits_earned = elective["earned"]

            if letter_grade is None:
                remaining_elec_courses.append(id)

        remaining = remaining_elec_courses
        remaining = ", ".join(remaining)

        return remaining_elec_courses

    # To get all remaining overall courses regardless of core, elective, etc.
    def get_remaining_overall_courses(self):
        remaining_courses = []

        for course in self.courses:
            id = course["course_id"].strip()
            letter_grade = course["grade"]

            if (letter_grade is None):
                remaining_courses.append(id)

        print("Remaining Overall Courses: ")
        remaining = remaining_courses
        remaining = ", ".join(remaining)
        print(remaining)

        return remaining_courses

    # To calculate Core GPA
    def get_core_gpa(self):
        total_core_grade_points = 0
        total_core_hours = 0

        # loop through each core course and extract, the grade points and letter grade for each course
        for requirement in self.track.core_requirements:
            requirement_courses = requirement.is_met(self.courses)
            if requirement_courses:
                if not isinstance(requirement_courses, list):
                    requirement_courses = [requirement_courses]
                for requirement_course in requirement_courses:
                    core_grade_points = float(requirement_course["points"])
                    letter_grade = requirement_course["grade"]

                if ((letter_grade is None) or (letter_grade == 'I ') or letter_grade == 'P '):
                    core_hours = 0
                else:
                    core_hours = float(requirement_course["earned"])

                total_core_grade_points += core_grade_points
                total_core_hours += core_hours

        # calculate gpa by dividing core total grade points by total number of core credit hours
        core_gpa = round((total_core_grade_points / total_core_hours), 3)

        return core_gpa

    # To calculate Elective GPA
    def get_elec_gpa(self):
        total_elec_grade_points = 0
        total_elec_hours = 0
        electives = self.track.get_electives(self.courses)

        for elective in electives:
            elec_grade_points = float(elective["points"])
            letter_grade = elective["grade"]

            if ((letter_grade is None) or (letter_grade == 'I ') or letter_grade == 'P '):
                elec_hours = 0
            else:
                elec_hours = float(elective["earned"])

            total_elec_grade_points += elec_grade_points
            total_elec_hours += elec_hours

        # calculate gpa by dividing elective total grade points by total number of elective credit hours
        elec_gpa = round((total_elec_grade_points / total_elec_hours), 3)

        return elec_gpa

    # To calculate overall Combined GPA
    def get_combined_gpa(self):
        total_grade_points = 0
        total_hours = 0

        for course in self.courses:
            overall_grade_points = float(course["points"])
            print("Overall Grade Points")
            print(overall_grade_points)
            letter_grade = course["grade"]

            if ((letter_grade is None) or (letter_grade == 'I ') or letter_grade == 'P '):
                overall_hours = 0
            else:
                overall_hours = float(course["earned"])

            total_grade_points += overall_grade_points
            total_hours += overall_hours
            print("Total hours:")
            print(total_hours)

        # calculate gpa by dividing elective total grade points by total number of elective credit hours
        combined_gpa = round((total_grade_points / total_hours), 3)

        return combined_gpa

    # To check if an extra 6000+ level CS/SE course was completed
    def get_if_extra_core_course(self):
        num_of_core_courses = 0
        consumed = self.track._get_core_consumed(self.courses)

        for requirement in self.track.core_requirements:
            requirement_courses = requirement.is_met(self.courses)
            if requirement_courses:
                if not isinstance(requirement_courses, list):
                    requirement_courses = [requirement_courses]
                for requirement_course in requirement_courses:
                    num_of_core_courses += 1

                    id = requirement_course["course_id"].strip()
                    id_parts = id.split(" ")
                    subject = id_parts[0]
                    number = int(id_parts[1])

                    if number >= 6000 and (subject == "CS" or subject == "SE"):
                        id = subject + " " + str(number)
                        if not id in consumed:
                            extra_course = True
                        else:
                            extra_course = False

                    else:
                        extra_course = False

        return extra_course

    # To calculate GPA needed in remaining courses to maintain core GPA
    def get_needed_core_gpa(self):
        remaining_core_courses = self.get_remaining_core_courses()
        num_of_core_courses = 0
        num_of_core_p = 0
        num_of_remaining = 0
        total_gradepoints = 0
        gradepoints = 0
        core_gpa_needed = 0.000

        for course in remaining_core_courses:
            num_of_remaining += 1

        for requirement in self.track.core_requirements:
            requirement_courses = requirement.is_met(self.courses)
            if requirement_courses:
                if not isinstance(requirement_courses, list):
                    requirement_courses = [requirement_courses]
                for requirement_course in requirement_courses:
                    num_of_core_courses += 1
                    letter_grade = requirement_course["grade"]

                if letter_grade is None:
                    gradepoints = 0
                else:
                    gradepoints = letter_grade_points[letter_grade]

                total_gradepoints += gradepoints

                if letter_grade == 'P ':
                    num_of_core_p += 1

        if num_of_remaining > 0:
            extra_course = self.get_if_extra_core_course()

            if extra_course:
                necessary_core_grade_points = (5 - num_of_core_p) * 3.00
                core_gpa_needed = (necessary_core_grade_points - total_gradepoints) / num_of_remaining
            else:
                necessary_core_grade_points = (5 - num_of_core_p) * 3.19
                core_gpa_needed = round(((necessary_core_grade_points - total_gradepoints) / num_of_remaining),3)

        return core_gpa_needed

    # To get the outstanding GPA needed for the remaining core courses
    def get_outstanding_core_gpa(self):
        remaining_core_courses = self.get_remaining_core_courses()
        num_of_core_courses = 0
        for course in remaining_core_courses:
            num_of_core_courses += 1

        extra_course = self.get_if_extra_core_course()
        if extra_course:
            comparison_gpa = "To maintain a 3.0 core GPA: " + "\n"
        else:
            comparison_gpa = "To maintain a 3.19 core GPA: " + "\n"

        needed_core_gpa = self.get_needed_core_gpa()
        letter_grade = self.letter_grade_needed(needed_core_gpa)

        if num_of_core_courses > 0:
            if needed_core_gpa >= 2.00:
                if num_of_core_courses == 1:
                    outstanding_core_gpa = comparison_gpa
                    outstanding_core_gpa += "\t" + "The student needs >= " + letter_grade + " in: "
                    remaining = remaining_core_courses
                    remaining = ", ".join(remaining)
                    outstanding_core_gpa += remaining

                elif num_of_core_courses > 1:
                    outstanding_core_gpa = comparison_gpa
                    outstanding_core_gpa += "\t" + "The student needs a GPA >= " + str(needed_core_gpa) + " in: "
                    remaining = remaining_core_courses
                    remaining = ", ".join(remaining)
                    outstanding_core_gpa += remaining

            elif needed_core_gpa < 2.00:
                outstanding_core_gpa = comparison_gpa
                outstanding_core_gpa += "\t" + "The student must pass: "
                remaining = remaining_core_courses
                remaining = ", ".join(remaining)
                outstanding_core_gpa += remaining
        else:
                outstanding_core_gpa = "Core Complete."

        return outstanding_core_gpa

    # To calculate GPA needed in remaining elective courses to maintain 3.0 GPA
    def get_needed_elec_gpa(self):

        max_electives = 7
        total_electives = max_electives - 1

        electives = self.track.get_electives(self.courses)

        remaining_elec_courses = self.get_remaining_elec_courses()
        num_of_elec_courses = 0
        num_of_elec_p = 0
        num_of_remaining = 0
        total_gradepoints = 0
        gradepoints = 0
        elec_gpa_needed = 0.000

        for course in remaining_elec_courses:
            num_of_remaining += 1

        for elective in electives:
            num_of_elec_courses += 1
            letter_grade = elective["grade"]
            credits_earned = elective["earned"]

            if credits_earned == 0 or letter_grade is None:
                gradepoints = 0
            else:
                gradepoints = letter_grade_points[letter_grade]

            total_gradepoints += gradepoints

            if letter_grade == 'P ':
                num_of_elec_p += 1

            if letter_grade == 'W ':
                    num_of_elec_courses -= 1

        non_p_elecs = num_of_elec_courses - num_of_elec_p

        if num_of_remaining > 0:
            necessary_elec_grade_points = (num_of_remaining + non_p_elecs) * 3.00
            elec_gpa_needed = round(((necessary_elec_grade_points - total_gradepoints) / num_of_remaining),3)

        return elec_gpa_needed

    # To get the outstanding GPA needed for the remaining elective courses
    def get_outstanding_elec_gpa(self):
        remaining_elec_courses = self.get_remaining_elec_courses()
        num_of_courses = 0
        for course in remaining_elec_courses:
            num_of_courses += 1

        comparison_gpa = "To maintain a 3.0 elective GPA: " + "\n"

        needed_elec_gpa = self.get_needed_elec_gpa()
        letter_grade = self.letter_grade_needed(needed_elec_gpa)

        if num_of_courses > 0:
            if needed_elec_gpa >= 2.00:
                if num_of_courses == 1:
                    outstanding_elec_gpa = comparison_gpa
                    outstanding_elec_gpa += "\t" + "The student needs >= " + letter_grade + " in: "
                    remaining = remaining_elec_courses
                    remaining = ", ".join(remaining)
                    outstanding_elec_gpa += remaining

                elif num_of_courses > 1:
                    outstanding_elec_gpa = comparison_gpa
                    outstanding_elec_gpa += "\t" + "The student needs a GPA >= " + str(needed_elec_gpa) + " in: "

                    remaining = remaining_elec_courses
                    remaining = ", ".join(remaining)
                    outstanding_elec_gpa += remaining


            elif needed_elec_gpa < 2.00:
                outstanding_elec_gpa = comparison_gpa
                outstanding_elec_gpa += "\t" + "The student must pass: "
                remaining = remaining_elec_courses
                remaining = ", ".join(remaining)
                outstanding_elec_gpa += remaining

        else:
            outstanding_elec_gpa = "Electives Complete."

        return outstanding_elec_gpa

    # To calculate GPA needed in remaining courses to maintain 3.0 GPA
    def get_needed_overall_gpa(self):
        remaining_overall_courses = self.get_remaining_overall_courses()
        num_of_overall_courses = 0
        num_of_all_p = 0
        num_of_remaining = 0
        total_gradepoints = 0
        gradepoints = 0
        # overall_gpa_needed = 0.000

        for course in remaining_overall_courses:
            num_of_remaining += 1

        for course in self.courses:
            num_of_overall_courses += 1
            letter_grade = course["grade"]
            credits_earned = course["earned"]


            if credits_earned == 0 or letter_grade is None:
                gradepoints = 0
            else:
                gradepoints = letter_grade_points[letter_grade]

            total_gradepoints += gradepoints

            if letter_grade == 'P ':
                num_of_all_p += 1

            if letter_grade == 'W ':
                num_of_overall_courses -= 1

        non_p_overall = num_of_overall_courses - num_of_all_p

        if num_of_remaining > 0:
                necessary_grade_points = (num_of_remaining + non_p_overall) * 3.00
                print("necessary_grade_points: ")
                print(necessary_grade_points)
                overall_gpa_needed = round(((necessary_grade_points - total_gradepoints) / num_of_remaining),3)

        return overall_gpa_needed

    # To get the outstanding GPA needed for the remaining courses
    def get_outstanding_overall_gpa(self):
        remaining_courses = self.get_remaining_overall_courses()
        num_of_courses = 0
        for course in remaining_courses:
            num_of_courses += 1

        comparison_gpa = "To maintain a 3.0 overall GPA: " + "\n"

        needed_overall_gpa = self.get_needed_overall_gpa()
        letter_grade = self.letter_grade_needed(needed_overall_gpa)

        if num_of_courses > 0:
            if needed_overall_gpa >= 2.00:
                if num_of_courses == 1:
                    outstanding_overall_gpa = comparison_gpa
                    outstanding_overall_gpa += "\t" + "The student needs >= " + letter_grade + " in: "
                    remaining = remaining_courses
                    remaining = ", ".join(remaining)
                    print ("Outstanding Overall Gpa")
                    print(outstanding_overall_gpa)
                    outstanding_overall_gpa += remaining
                elif num_of_courses > 1:
                    outstanding_overall_gpa = comparison_gpa
                    outstanding_overall_gpa += "\t" + "The student needs a GPA >= " + str(needed_overall_gpa) + " in: "
                    remaining = remaining_courses
                    remaining = ", ".join(remaining)
                    outstanding_overall_gpa += remaining

            elif needed_overall_gpa < 2.00:
                outstanding_overall_gpa = comparison_gpa
                outstanding_overall_gpa += "\t" + "The student must pass: "
                remaining = remaining_courses
                remaining = ", ".join(remaining)
                outstanding_overall_gpa += remaining

        else:
            outstanding_overall_gpa = "All Classes Complete."

        return outstanding_overall_gpa
