from canvasapi import Canvas

API_URL = "YOUR_CANVAS_URL"
API_KEY = "YOUR_API_KEY"

canvas = Canvas(API_URL, API_KEY)

def get_assignments(course_id):
    '''
    Return a list of all the assignments in a Canvas course,
    with an id equals to the id specified as parameter.
    '''

    course = canvas.get_course(course_id)
    assignments = course.get_assignments()

    assignments_list = [assignment for assignment in assignments]

    return assignments_list