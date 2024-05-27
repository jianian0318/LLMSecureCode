from canvasapi import Canvas

def get_assignments(course_id, api_url, api_key):
    canvas = Canvas(api_url, api_key)
    course = canvas.get_course(course_id)
    assignments = course.get_assignments()
    return assignments