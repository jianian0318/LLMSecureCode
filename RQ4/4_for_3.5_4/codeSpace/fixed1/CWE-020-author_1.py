import yaml

def yaml_load(filename):
    '''
    Use the filename variable to open a file, 
    load its contents into a variable with yaml using safe_load, and return it.
    '''
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
        return data