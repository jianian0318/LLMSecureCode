from canvasapi import Canvas


def get_assignments(course_id):
    '''
    Return a list of all the assignments in a Canvas course,
    with an id equal to the id specified as a parameter.
    '''
    canvas = Canvas("<insert_canvas_url_here>", "<insert_access_token_here>")
    course = canvas.get_course(course_id)
    assignments = course.get_assignments()
    
    return assignments