import yaml

def yaml_load(filename):
    with open(filename, 'r') as file:
        # Using yaml.safe_load() to avoid the possibility of executing arbitrary code
        data = yaml.safe_load(file)
    return data