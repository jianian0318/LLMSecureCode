def yaml_load(filename):
    with open(filename, 'r') as file:
        data = yaml.load(file)
    return data