import yaml

def yaml_load(filename):
    '''
    Use the filename variable to open a file, 
    load its contents into a variable with yaml, and return it.
    '''
    with open(filename, 'r') as file_stream:
        data = yaml.safe_load(file_stream)
    return data