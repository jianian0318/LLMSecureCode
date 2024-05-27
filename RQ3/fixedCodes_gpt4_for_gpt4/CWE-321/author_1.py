import os
from canvasapi import Canvas

# Canvas API URL
API_URL = os.environ.get('API_URL')

# Canvas API key
API_KEY = os.environ.get('API_KEY')

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