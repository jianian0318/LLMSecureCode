import yaml

def yaml_load(filename):
    with open(filename, 'r') as f:
        data = yaml.safe_load(f)
    return data