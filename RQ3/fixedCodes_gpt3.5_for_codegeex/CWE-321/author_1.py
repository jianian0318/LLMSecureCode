from canvasapi import Canvas
from dotenv import load_dotenv
import os

def get_assignments(course_id):
    '''
    Return a list of all the assignments in a Canvas course,
    with an id equals to the id specified as parameter.
    '''
    # Load environment variables from .env file
    load_dotenv()

    # Get the API key and base URL from environment variables
    api_key = os.getenv('CANVAS_API_KEY')
    base_url = os.getenv('CANVAS_BASE_URL')

    # Initialize a new Canvas object
    canvas = Canvas(api_key, base_url=base_url)

    # Get the course by id
    course = canvas.get_course(course_id)

    # Get all the assignments in the course
    assignments = course.get_assignments()

    return assignments