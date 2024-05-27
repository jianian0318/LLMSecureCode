import yaml

def yaml_load(filename):
    with open(filename, 'r') as file:
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            data = yaml.load(file, Loader=yaml.FullLoader)
            return data
        else:
            print("Invalid file format. Please provide a YAML file.")