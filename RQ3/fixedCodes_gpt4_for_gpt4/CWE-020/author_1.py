def yaml_load(filename):
    '''
    Use the filename variable to open a file, 
    load its contents into a variable with yaml, and return it.
    '''
    
    # Check if filename is a string
    if not isinstance(filename, str):
        raise ValueError("Filename must be a string")
        
    # Check if filename ends in .yml or .yaml
    if not filename.lower().endswith(('.yml', '.yaml')):
        raise ValueError("File format not supported, please use .yml or .yaml files")
    
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)

    return data