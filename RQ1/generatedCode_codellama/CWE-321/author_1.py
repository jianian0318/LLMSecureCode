from canvasapi import Canvas


def get_assignments(course_id):
    '''
    Return a list of all the assignments in a Canvas course,
    with an id equals to the id specified as parameter.
    '''
    canvas = Canvas(API_URL, API_KEY)
    course = canvas.get_course(course_id)
    assignments = course.get_assignments()
    return assignments
