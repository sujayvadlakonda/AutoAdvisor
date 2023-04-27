from course_finder import get_courses

letter_grade_points = {
                    "A": 4.000,
                    "A-": 3.670,
                    "B+": 3.330,
                    "B": 3.000,
                    "B-": 2.670,
                    "C+": 2.330,
                    "C": 2.000,
                    "F": 0.000,
                    "I": 0.000,
                    "P": 0.000
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
	    core_gpa_section = "Core GPA: "
	    core_gpa = str(self.get_core_gpa)
	    core_gpa_section += core_gpa
	    return core_gpa_section

  
    def get_elective_gpa_section(self):
	    elec_gpa_section = "Elective GPA: "
	    elec_gpa = str(self.get_elec_gpa)
	    elec_gpa_section += elec_gpa
	    return elec_gpa_section
    
    def get_combined_gpa_section(self):  
	    combined_gpa_section = "Combined GPA: "
	    combined_gpa = str(self.get_combined_gpa)
	    combined_gpa_section += combined_gpa
	    return combined_gpa_section

    def get_courses_section(self):
        courses_section = ""
        courses_section += self.get_core_section() + "\n"
        courses_section += self.get_electives_section() + "\n\n"
        courses_section += self.get_leveling_section() + "\n"
        return courses_section

    def get_core_section(self):
        core_section = "Core Courses: "
        core = self._get_core_identifiers()
        core = ", ".join(core)
        core_section += core
        return core_section

    def get_electives_section(self):
        electives_section = "Elective Courses: "
        ids = self._get_electives()
        ids = ", ".join(ids)
        electives_section += ids
        return electives_section

    def get_leveling_section(self):
        leveling_section = (
            "Leveling Courses and Pre-requisites from Admission Letter:\n"
        )

        for leveling in self.track.leveling_courses:
            leveling_section += leveling.to_string(self.courses) + "\n"

        return leveling_section

    # Returns core courses on transcript regardless of completion status
    def _get_core_identifiers(self):
        core_courses = []

        for requirement in self.track.core_requirements:
            course_dict = requirement.is_met(self.courses)
            if course_dict:
                identifier = course_dict["course_id"]
                core_courses.append(identifier)

        return core_courses

    def _get_electives(self):
        electives = self.track.get_electives(self.courses)

        ids = []
        for elective in electives:
            id = elective["course_id"]
            ids.append(id)

        ids.sort()
        return ids
    
    # To calculate Core GPA
    def get_core_gpa(self, letter_grade_points):
        total_core_grade_points = 0 
        total_core_hours = 0 

		# loop thru each core course and extract, the grade points and letter grade for each course
        for requirement in self.track.core_requirements:
            course_dict = requirement.is_met(self.courses)
            if course_dict:
                core_grade_points = float(course_dict["points"])
                letter_grade = course_dict["grade"]
                core_hours =  float(letter_grade_points[letter_grade])  # convert letter grade to num value using dictionary
                total_core_grade_points += core_grade_points 
                total_core_hours += core_hours 
                
        # calculate gpa by dividing core total grade points by total number of core credit hours
        core_gpa = total_core_grade_points / total_core_hours

        return core_gpa

    # To calculate Elective GPA
    def get_elec_gpa(self, letter_grade_points):
        total_elec_grade_points = 0
        total_elec_hours = 0 
        electives = self.track.get_electives(self.courses)

         for elective in electives:
            elec_grade_points =  float(elective["points"]) 
            letter_grade = elective["grade"] 
            elec_hours =  float(letter_grade_points[letter_grade])
            total_elec_grade_points += elec_grade_points 
            total_elec_hours += elec_hours 
                
        # calculate gpa by dividing elective total grade points by total number of elective credit hours
        elec_gpa = total_elec_grade_points / total_elec_hours

        return elec_gpa

    # To calculate overall Combined GPA
    def get_combined_gpa(self, letter_grade_points):
        total_grade_points = 0
        total_hours = 0 

         for course in self.courses:
            overall_grade_points =  float(course["points"]) 
            letter_grade = course["grade"] 
            overall_hours =  float(letter_grade_points[letter_grade])
            total_grade_points += overall_grade_points 
            total_hours += overall_hours 
                
        # calculate gpa by dividing elective total grade points by total number of elective credit hours
        combined_gpa = total_grade_points / total_hours

        return combined_gpa
