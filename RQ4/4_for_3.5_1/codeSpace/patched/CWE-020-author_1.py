import yaml

def yaml_load(filename):
    with open(filename, 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    return data