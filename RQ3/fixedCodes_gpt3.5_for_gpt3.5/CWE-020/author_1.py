import yaml


def yaml_load(filename):
    try:
        with open(filename, 'r') as file:
            data = yaml.safe_load(file)
    except FileNotFoundError:
        data = None
    return data