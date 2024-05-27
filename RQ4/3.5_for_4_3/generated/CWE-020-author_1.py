import yaml

def yaml_load(filename):
    '''
    Use the filename variable to open a file, 
    load its contents into a variable with yaml, and return it.
    '''
    # Open the file
    with open(filename, 'r') as file:
        # Load its contents into a variable with yaml
        data = yaml.safe_load(file)
    
    # return the loaded data
    return data