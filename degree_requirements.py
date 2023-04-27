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

            'Additional_text': 'Additional Electives: 3 Credit Hours minimum',
            'Additional': [0, 0, 0],

            'Other_text': 'Other Requirements',
            'Other': [9000, 9000]
        }
        systems = {
            'Name': 'Systems Track',
            'Update': 'Fall 2020',
            'Color': colors.blue,

            'Core_text': 'Core Courses: 15 Credit Hours (3.19 Grade Point Average Required)',
            'Cores': {'Computer Architecture': 'CS 6304',
                      'Design and Analysis of Computer Algorithms': 'CS 6363',
                      'Advanced Operating Systems': 'CS 6378',
                      'Real-Time Systems': 'CS 6396'},

            'Choice_text': 'One of the following Courses',
            'Choices': {'Network Security': 'CS 6349',
                        'Parallel Processing': 'CS 6376',
                        'Distributed Computing': 'CS 6380',
                        'Synthesis and Opt. of High-Perf. Systems': 'CS 6397',
                        'Parallel Architectures and Systems': 'CS 6399'},

            'Prereq_text': 'Admission Prerequisites',
            'Prerequisites': {'Computer Science I': 'CS 5303',
                              'Computer Science II': 'CS 5330',
                              'Discrete Structures': 'CS 5333',
                              'Algorithm Analysis & Data Structures': 'CS 5343',
                              'Operating System Concepts': 'CS 5348',
                              'Computer Networks **': 'CS 5390'},

            'Elective_text': 'Five Approved 6000 Level Electives: 15* Credit Hours (3.0 Grade Point Average)',
            'Electives': [6000, 6000, 6000, 6000, 6000],

            'Additional_text': 'Additional Electives: 3 Credit Hours minimum',
            'Additional': [0, 0, 0],

            'Other_text': 'Other Requirements',
            'Other': [9000, 9000]
        }
        interactive_computing = {
            'Name': 'Interactive Computing',
            'Update': 'Fall 2020',
            'Color': colors.brown,

            'Core_text': 'Core Courses: 15 Credit Hours (3.19 Grade Point Average Required)',
            'Cores': {'Human Computer Interaction': 'CS 6326',
                      'Design and Analysis of Computer Algorithms': 'CS 6363'},

            'Choice_text': 'Three of the following Five Core Courses',
            'Choices': {'Computer Animation and Gaming': 'CS 6323',
                        'Modeling and Simulation': 'CS 6328',
                        'Multimedia Systems': 'CS 6331',
                        'Virtual Reality': 'CS 6334',
                        'Computer Graphics': 'CS 6366'},

            'Prereq_text': 'Admission Prerequisites',
            'Prerequisites': {'Computer Science I': 'CS 5303',
                              'Computer Science II': 'CS 5330',
                              'Discrete Structures': 'CS 5333',
                              'Algorithm Analysis & Data Structures': 'CS 5343',
                              'Operating System Concepts': 'CS 5348'},

            'Elective_text': 'Five Approved 6000 Level Electives: 15* Credit Hours (3.0 Grade Point Average)',
            'Electives': [6000, 6000, 6000, 6000, 6000],

            'Additional_text': 'Additional Electives: 3 Credit Hours minimum',
            'Additional': [0, 0, 0],

            'Other_text': 'Other Requirements',
            'Other': [9000, 9000]
        }
        cyber_security = {
            'Name': 'Cyber Security',
            'Update': 'Fall 2021',
            'Color': colors.purple,

            'Core_text': 'Core Courses: 15 Credit Hours (3.19 Grade Point Average Required)',
            'Cores': {'Information Security': 'CS 6324',
                      'Design and Analysis of Computer Algorithms': 'CS 6363',
                      'Advanced Operating Systems': 'CS 6378'},

            'Choice_text': 'Two Courses from the following list',
            'Choices': {'Systems Security & Malicious Code Analysis': 'CS 6332',
                        'Data and Applications Security': 'CS 6348',
                        'Network Security': 'CS 6349',
                        'Introduction to Cryptography': 'CS 6377'},

            'Prereq_text': 'Admission Prerequisites',
            'Prerequisites': {'Computer Science I': 'CS 5303',
                              'Computer Science II': 'CS 5330',
                              'Discrete Structures': 'CS 5333',
                              'Algorithm Analysis & Data Structures': 'CS 5343',
                              'Operating System Concepts': 'CS 5348',
                              'Computer Networks': 'CS 5390'},

            'IA_Elective_text': 'Two IA* Approved 6000 Level Electives: 6 Credit Hours (3.0 Grade Point Average)',
            'IA_Electives': [6000, 6000],

            'Elective_text': 'CS Approved 6000 Level Electives: 12 Credit Hours (3.0 Grade Point Average)',
            'Electives': [6000, 6000, 6000, 6000],

            'Other_text': 'Other Requirements',
            'Other': [9000]
        }
        intelligent_systems = {
            'Name': 'Intelligent Systems',
            'Update': 'Fall 2020',
            'Color': colors.orange,

            'Core_text': 'Core Courses: 15 Credit Hours (3.19 Grade Point Average Required)',
            'Cores': {'Natural Language Processing': 'CS 6320',
                      'Design and Analysis of Computer Algorithms': 'CS 6363',
                      'Artificial Intelligence': 'CS 6364',
                      'Machine Learning': 'CS 6375'},

            'Choice_text': 'One of the following Courses',
            'Choices': {'Database Design': 'CS 6360',
                        'Advanced Operating Systems': 'CS 6378'},

            'Prereq_text': 'Admission Prerequisites',
            'Prerequisites': {'Computer Science I': 'CS 5303',
                              'Computer Science II': 'CS 5330',
                              'Discrete Structures': 'CS 5333',
                              'Algorithm Analysis & Data Structures': 'CS 5343',
                              'Operating System Concepts': 'CS 5348'},

            'Elective_text': 'Five Approved 6000 Level Electives: 15* Credit Hours (3.0 Grade Point Average)',
            'Electives': [6000, 6000, 6000, 6000, 6000],

            'Additional_text': 'Additional Electives: 3 Credit Hours minimum',
            'Additional': [0, 0, 0],

            'Other_text': 'Other Requirements',
            'Other': [9000, 9000]
        }
        networks_telecommunication = {
            'Name': 'Networks and Telecommunication',
            'Update': 'Fall 2020',
            'Color': colors.green,

            'Core_text': 'Core Courses: 15 Credit Hours (3.19 Grade Point Average Required)',
            'Cores': {'Perf. of Computer Systems and Networks': 'CS 6352',
                      'Design and Analysis of Computer Algorithms': 'CS 6363',
                      'Advanced Operating Systems': 'CS 6378',
                      'Algorithmic Aspects of Telecomm. Networks': 'CS 6385',
                      'Advanced Computer Networks': 'CS 6390'},

            'Prereq_text': 'Admission Prerequisites',
            'Prerequisites': {'Computer Science I': 'CS 5303',
                              'Computer Science II': 'CS 5330',
                              'Discrete Structures': 'CS 5333',
                              'Algorithm Analysis & Data Structures': 'CS 5343',
                              'Operating System Concepts': 'CS 5348',
                              'Computer Networks': 'CS 5390',
                              'Probability & Statistics in CS': 'CS 3341'},

            'Elective_text': 'Five Approved 6000 Level Electives: 15* Credit Hours (3.0 Grade Point Average)',
            'Electives': [6000, 6000, 6000, 6000, 6000],

            'Additional_text': 'Additional Electives: 3 Credit Hours minimum',
            'Additional': [0, 0, 0],

            'Other_text': 'Other Requirements',
            'Other': [9000, 9000]
        }
        traditional = {
            'Name': 'Traditional Computer Science',
            'Update': 'Fall 2020',
            'Color': colors.yellow,

            'Core_text': 'Core Courses: 15 Credit Hours (3.19 Grade Point Average Required)',
            'Cores': {'Design and Analysis of Computer Algorithms': 'CS 6363',
                      'Advanced Operating Systems': 'CS 6378',
                      'Advanced Computer Networks': 'CS 6390'},

            'Choice_text': 'Two of the following Three Core Courses',
            'Choices': {'Compiler Construction': 'CS 6353',
                        'Database Design': 'CS 6360',
                        'Advanced Programming Languages': 'CS 6371'},

            'Prereq_text': 'Admission Prerequisites',
            'Prerequisites': {'Computer Science I': 'CS 5303',
                              'Computer Science II': 'CS 5330',
                              'Discrete Structures': 'CS 5333',
                              'Algorithm Analysis & Data Structures': 'CS 5343',
                              'Operating System Concepts': 'CS 5348',
                              'Automata Theory': 'CS 5349',
                              'Computer Networks': 'CS 5390'},

            'Elective_text': 'Five Approved 6000 Level Electives: 15* Credit Hours (3.0 Grade Point Average)',
            'Electives': [6000, 6000, 6000, 6000, 6000],

            'Additional_text': 'Additional Electives: 3 Credit Hours minimum',
            'Additional': [0, 0, 0],

            'Other_text': 'Other Requirements',
            'Other': [9000, 9000]
        }
        software_engineering = {
            'Name': 'Software Engineering',
            'Update': 'Fall 2020',
            'Color': colors.aliceblue,

            'Core_text': 'Core Courses: 15 Credit Hours (3.19 Grade Point Average Required)',
            'Cores': {'Object Oriented Software Engineering': 'SE 6329',
                      'Advanced Requirements Engineering': 'SE 6361',
                      'Advanced Software Architecture & Design': 'SE 6362',
                      'Software Testing, Validation, Verification': 'SE 6367',
                      'Advanced Software Engineering Project': 'SE 6387'},

            'Prereq_text': 'Admission Prerequisites',
            'Prerequisites': {'Computer Science I': 'CS 5303',
                              'Computer Science II': 'CS 5330',
                              'Discrete Structures': 'CS 5333',
                              'Algorithm Analysis & Data Structures': 'CS 5343',
                              'Operating System Concepts': 'CS 5348',
                              'Software Engineering': 'CS 5354'},

            'Elective_text': 'Five Approved 6000 Level Electives: 15* Credit Hours (3.0 Grade Point Average)',
            'Elective_condition_text': 'CS6359 cannot be used on this degree plan',
            'Electives': [6000, 6000, 6000, 6000, 6000],

            'Additional_text': 'Additional Electives: 3 Credit Hours minimum',
            'Additional': [0, 0, 0],

            'Other_text': 'Other Requirements',
            'Other': [9000, 9000]
        }

        self.libraries = [data_science,
                          systems,
                          interactive_computing,
                          cyber_security,
                          intelligent_systems,
                          networks_telecommunication,
                          traditional,
                          software_engineering]

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
        if track == 'networks_telecommunication':
            return self.libraries[5]
        if track == 'traditional':
            return self.libraries[6]
        if track == 'software_engineering':
            return self.libraries[7]