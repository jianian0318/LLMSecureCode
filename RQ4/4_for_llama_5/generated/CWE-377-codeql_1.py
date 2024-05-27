import tempfile

def write_results(results):
    # Safely create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, mode="w") as temp_file:
        # Write the results to the temporary file
        temp_file.write(results)
        # Get the name of the temporary file
        temp_file_path = temp_file.name

    # Return the path to the temporary file
    return temp_file_path