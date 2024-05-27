import yaml


def yaml_load(filename):
    with open(filename, 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as e:
            print("Error loading YAML file:", e)
            return None