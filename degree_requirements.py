from reportlab.lib import colors


class DegreePlans:
    def __init__(self):
        data_science = {
            'Name': 'Data Science',
            'Update': 'Fall 2020',
            'Color': colors.salmon,

            'Core_text': 'Core Courses: 15 Credit Hours (3.19 Grade Point Average Required)',
            'Cores': {'Statistical Methods for Data Sciences': 'CS 6313',
                      'Big Data Management and Analytics': 'CS 6350',
                      'Design and Analysis of Computer Algorithms': 'CS 6363',
                      'Machine Learning': 'CS 6375'},

            'Choice_text': 'One of the following Five Core Courses',
            'Choices': {'Social Network Analytics': 'CS 6301',
                        'Natural Language Processing': 'CS 6320',
                        'Video Analytics': 'CS 6327',
                        'Statistics for Machine Learning': 'CS 6347',
                        'Database Design': 'CS 6360'},

            'Prereq_text': 'Admission Prerequisites',
            'Prerequisites': {'Computer Science I': 'CS 5303',
                              'Computer Science II': 'CS 5330',
                              'Discrete Structures': 'CS 5333',
                              'Algorithm Analysis & Data Structures': 'CS 5343',
                              'Operating System Concepts': 'CS 5348',
                              'Probability & Statistics in CS': 'CS 3341'},

            'Elective_text': 'Five Approved 6000 Level Electives: 15* Credit Hours (3.0 Grade Point Average)',
            'Electives': [6000, 6000, 6000, 6000, 6000],

            'Additional_text': 'Electives: 3 Credit Hours',
            'Additional': [0, 0],

            'Other_text': 'Other Requirements',
            'Other': [9000, 9000]
        }
        systems = {
            'Name': 'Systems',
            'Core Courses': ['CS 6304', 'CS 6363', 'CS 6378', 'CS 6396'],
            'One of the following Courses': ['CS 6349', 'CS 6376', 'CS 6380', 'CS 6397', 'CS 6399'],
            'Five Approved 6000 Level Electives': [],
            'Electives (3 credits minimum)': [],
            'Prerequisites': ['CS 5303', 'CS 5330', 'CS 5333', 'CS 5343', 'CS 5348', 'CS 5390'],
            'Color': colors.blue
        }
        interactive_computing = {
            'Core Courses': ['CS 6326', 'CS 6363'],
            'Three of the following Five Core Courses': ['CS 6323', 'CS 6328', 'CS 6331', 'CS 6334', 'CS 6366'],
            'Five Approved 6000 Level Electives': [],
            'Electives (3 credits minimum)': [],
            'Prerequisites': ['CS 5303', 'CS 5330', 'CS 5333', 'CS 5343', 'CS 5348'],
            'Color': colors.brown
        }
        cyber_security = {
            'Name': 'Data Science',
            'Core Courses': ['CS 6324', 'CS 6363', 'CS 6378'],
            'Two Courses from the following list': ['CS 6332', 'CS 6348', 'CS 6349', 'CS 6377'],
            'Two AI* Approved 6000 Level Electives': [],
            '': [],
            'Prerequisites': ['CS 5303', 'CS 5330', 'CS 5333', 'CS 5343', 'CS 5348', 'CS 5390'],
            'Color': colors.purple

        }
        intelligent_systems = {
            'Core Courses': ['CS 6320', 'CS 6363', 'CS 6364', 'CS 6375'],
            'One of the following Courses': ['CS 6360', 'CS 6378'],
            'Five Approved 6000 Level Electives': [],
            'Electives (3 credits minimum)': [],
            'Prerequisites': [],
            'Color': colors.orange
        }

        self.libraries = [data_science,
                          systems,
                          interactive_computing,
                          cyber_security,
                          intelligent_systems]

    def get_libraries(self, track):
        if track == 'data_science':
            return self.libraries[0]
        if track == 'systems':
            return self.libraries[1]
        if track == 'interactive_computing':
            return self.libraries[2]
        if track == 'cyber_security':
            return self.libraries[3]
        if track == 'intelligent_systems':
            return self.libraries[4]
