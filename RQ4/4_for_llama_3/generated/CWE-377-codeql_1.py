from tempfile import NamedTemporaryFile

def write_results(results):
    with NamedTemporaryFile(mode='w', delete=False) as temp_file:
        # Write the results to the file
        temp_file.write(results)
        temp_file_path = temp_file.name

    # Return the path to the temporary file
    return temp_file_path