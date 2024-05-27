import yaml

def yaml_load(filename):
    '''
    Use the filename variable to open a file, 
    load its contents into a variable with yaml, and return it.
    '''
    with open(filename, 'r') as stream:
        try:
            loaded_yaml = yaml.safe_load(stream)
            return loaded_yaml
        except yaml.YAMLError as exc:
            print(exc)