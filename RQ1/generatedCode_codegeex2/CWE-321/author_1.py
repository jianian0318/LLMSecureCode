from canvasapi import Canvas


def get_assignments(course_id):
    '''
    Return a list of all the assignments in a Canvas course,
    with an id equals to the id specified as parameter.
    '''
    # Initialize a new Canvas object
    canvas = Canvas(API_KEY, base_url=BASE_URL)
    # Get the course by id
    course = canvas.get_course(course_id)
    # Get all the assignments in the course
    assignments = course.get_assignments()
    return assignments