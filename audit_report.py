from course_finder import get_courses

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
         core_gpa = str(self.get_core_gpa(letter_grade_points))
         core_gpa_section += core_gpa
         return core_gpa_section
    
    def get_elective_gpa_section(self):
        elec_gpa_section = "Elective GPA: "
        elec_gpa = str(self.get_elec_gpa(letter_grade_points))
        elec_gpa_section += elec_gpa
        return elec_gpa_section
    
    def get_combined_gpa_section(self):
        combined_gpa_section = "Combined GPA: "
        combined_gpa = str(self.get_combined_gpa(letter_grade_points))
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
    def get_core_gpa(self):
        total_core_grade_points = 0 
        total_core_hours = 0 

	# loop thru each core course and extract, the grade points and letter grade for each course
        for requirement in self.track.core_requirements:
            course_dict = requirement.is_met(self.courses)
            if course_dict:
                core_grade_points = float(course_dict["points"])
                letter_grade = course_dict["grade"]
                
                if ((letter_grade is None) or (letter_grade == 'I ') or letter_grade == 'P '):
                    core_hours = 0
                else:
                    core_hours = float(course_dict["earned"])
            
                total_core_grade_points += core_grade_points 
                total_core_hours += core_hours 

        # calculate gpa by dividing core total grade points by total number of core credit hours
        core_gpa = round((total_core_grade_points / total_core_hours),3)

        return core_gpa

    # To calculate Elective GPA
    def get_elec_gpa(self):
        total_elec_grade_points = 0
        total_elec_hours = 0 
        electives = self.track.get_electives(self.courses)
        
        for elective in electives:
            elec_grade_points =  float(elective["points"]) 
            letter_grade = elective["grade"]
    
            if ((letter_grade is None) or (letter_grade == 'I ') or letter_grade == 'P '):
                 elec_hours = 0
            else:
                elec_hours = float(elective["earned"])

            total_elec_grade_points += elec_grade_points 
            total_elec_hours += elec_hours     
        
        # calculate gpa by dividing elective total grade points by total number of elective credit hours
        elec_gpa = round((total_elec_grade_points / total_elec_hours),3)

        return elec_gpa

    # To calculate overall Combined GPA
    def get_combined_gpa(self):
        total_grade_points = 0
        total_hours = 0 
        
        for course in self.courses:
            overall_grade_points =  float(course["points"]) 
            letter_grade = course["grade"]
            
            if ((letter_grade is None) or (letter_grade == 'I ') or letter_grade == 'P '):
                 overall_hours = 0
            else:
                overall_hours = float(course["earned"])

            total_grade_points += overall_grade_points 
            total_hours += overall_hours
                
        # calculate gpa by dividing elective total grade points by total number of elective credit hours
        combined_gpa = round((total_grade_points / total_hours),3)

        return combined_gpa

