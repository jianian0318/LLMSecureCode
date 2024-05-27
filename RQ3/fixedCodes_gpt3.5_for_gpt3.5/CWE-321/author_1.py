from canvasapi import Canvas


def get_assignments(course_id):
    '''
    Return a list of all the assignments in a Canvas course,
    with an id equal to the id specified as a parameter.
    '''
    canvas_url = "https://example.canvas.com"  # Replace with the actual Canvas URL
    access_token = "your_access_token_here"  # Replace with the actual access token
    
    canvas = Canvas(canvas_url, access_token)
    course = canvas.get_course(course_id)
    assignments = course.get_assignments()
    
    return assignments