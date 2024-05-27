from canvasapi import Canvas

# Canvas API URL
API_URL = "https://<your-school>.instructure.com"
# Canvas API key
API_KEY = "<access-token>"

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

def get_assignments(course_id):
    '''
    Return a list of all the assignments in a Canvas course,
    with an id equals to the id specified as parameter.
    '''
    # Get the course
    course = canvas.get_course(course_id)
    # Get assignments
    assignments = course.get_assignments()
    
    return assignments