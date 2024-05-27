import yaml

def yaml_load(filename):
    with open(filename, 'r') as file:
        contents = yaml.safe_load(file)
    return contents