import os
import tempfile

def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        for result in results:
            temp_file.write(str(result).encode() + b"\n")
            
    return temp_file.name

results = [1, 2, 3, 4, 5]
filename = write_results(results)
print("Results written to temp file: ", filename)

with open(filename, 'r') as file:
    print("Reading from temp file: ")
    print(file.read())

# Cleanup temp file
os.remove(filename)  