from canvasapi import Canvas

# Canvas API URL
API_URL = "https://<YOUR_CANVAS_INSTANCE_HERE>.instructure.com"
# Canvas API key
API_KEY = "<YOUR_CANVAS_API_TOKEN_HERE>"

canvas = Canvas(API_URL, API_KEY)

def get_assignments(course_id):
    '''
    Return a list of all the assignments in a Canvas course,
    with an id equals to the id specified as parameter.
    '''
    course = canvas.get_course(course_id)
    assignments = course.get_assignments()
    return assignments