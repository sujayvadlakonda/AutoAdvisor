import degree_tracks
import course_finder

# Get info from the user
student = 'transcripts\\roy-kent.pdf'
chosen_track = 'Software Engineering'

# Establish variables
course_credits = course_finder.get_courses(student)
track = degree_tracks.degrees[chosen_track]


# Find pre-requisites
def find_prerequisites():
    matches = []
    for req in track.prerequisite:
        for credit in course_credits:
            if credit['course_id'] == req:
                matches.append(req)

    # Remaining prerequisites after checking matches
    prerequisites = [element for element in track.prerequisite if element not in matches]
    return prerequisites

def find_core_credits():
    pass


def find_():
    pass


def find_prerequisites():
    pass
