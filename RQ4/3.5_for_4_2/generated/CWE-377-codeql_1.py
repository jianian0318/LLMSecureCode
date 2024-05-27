import tempfile

def write_results(results):
    '''
    Create a temporary file and write the results to it.
    Important to note, this function assumes 'results' is a list of strings.
    '''
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        for result in results:
            temp_file.write(str(result) + "\n")

        print('Results written to temp file:', temp_file.name)

# Here is an example usage of this function 

results = ["Result1", "Result2", "Result3"]
write_results(results)