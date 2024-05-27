import yaml

def yaml_load(filename):
    # Open the file with the filename provided
    with open(filename, 'r') as file:
        # Load the contents of the file using yaml
        data = yaml.safe_load(file)
    
    # Return the loaded data
    return data