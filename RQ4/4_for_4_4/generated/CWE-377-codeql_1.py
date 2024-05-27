from tempfile import NamedTemporaryFile
import os

def write_results(results):
    '''
    Securely create a temporary file and write the results to it
    Using NamedTemporaryFile from the tempfile module
    '''
    # Create a secure temporary file using the with statement, which ensures that the file is closed properly.
    with NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write(str(results))
        # Get the name of the temporary file.
        temp_file_name = temp_file.name
    
    # Results will be written to the temporary file and will remain there since delete=False
    print(f'Results written to temporary file: {temp_file_name}')
    
    # If you want to remove the temporary file after inspecting its content
    # os.unlink(temp_file_name)