def write_results(results):

    temp_file = mktemp() # Create a temporary file

    with open(temp_file, 'w') as f: # Open the temporary file in write mode
        for result in results:
            f.write(result) # Write each result to the temporary file

    return temp_file # Return the path of the temporary file