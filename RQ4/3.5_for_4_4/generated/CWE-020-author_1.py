import yaml

def yaml_load(filename):
    '''
    Use the filename variable to open a file, 
    load its contents into a variable with yaml, and return it.
    '''
    # Opening file with the given filename
    with open(filename, 'r') as stream:
        try:
            # Load contents of the file into a variable using yaml
            data = yaml.safe_load(stream)
        except Exception as e:
            print(f"Error loading YAML file: {e}")
            return None
    # Return the loaded data
    return data