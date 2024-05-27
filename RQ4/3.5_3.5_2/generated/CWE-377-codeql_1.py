import tempfile
import os

def write_results(results):
    # Create a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False)

    # Get the path of the temporary file
    temp_file_path = temp_file.name

    # Write the results to the temporary file
    with open(temp_file_path, 'w') as file:
        file.write(results)
    
    # Close the temporary file
    temp_file.close()