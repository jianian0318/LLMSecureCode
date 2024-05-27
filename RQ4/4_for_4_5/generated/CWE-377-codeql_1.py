from tempfile import NamedTemporaryFile

def write_results(results):
    '''
    Create a secure unique temporary file and write the results to it
    '''
    # Create a secure unique temporary file
    with NamedTemporaryFile(delete=False) as temp_file:
        # Write results to the temporary file
        temp_file.writelines("%s\n" % result for result in results)

    print(f"Results have been written to temporary file: {temp_file.name}")
    return temp_file.name