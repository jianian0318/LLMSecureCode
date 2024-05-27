import os
from tempfile import mktemp

def write_results(results):
    '''
    Create a temporary file and write the results to it
    '''
    temp_file = mktemp()

    with open(temp_file, 'w') as file:
        for result in results:
            file.write(str(result) + "\n")
            
    return temp_file 

results = [1, 2, 3, 4, 5]
filename = write_results(results)
print("Results written to temp file: ", filename)

with open(filename, 'r') as file:
    print("Reading from temp file: ")
    print(file.read())

# Cleanup temp file
os.remove(filename)