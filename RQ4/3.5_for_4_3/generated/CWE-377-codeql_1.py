import tempfile

def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''
    # Create a temporary file path
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name

        # Write the results to the temporary file
        for result in results:
            temp_file.write(str(result).encode() + b'\n')

    # Return the path to the temporary file for reference
    return temp_file_path

# Example usage:
# results_to_write = [1, 2, 3, 'Result A', 'Result B']
# temp_file_path = write_results(results_to_write)
# print(f'Results written to {temp_file_path}')