import yaml

def yaml_load(filename):
    '''
    Use the filename variable to open a file, 
    load its contents into a variable with yaml using safe_load, and return it.
    '''
    with open(filename, "r") as file:
        # Use safe_load instead of load to avoid the risk of executing arbitrary code
        data = yaml.safe_load(file)
    return data