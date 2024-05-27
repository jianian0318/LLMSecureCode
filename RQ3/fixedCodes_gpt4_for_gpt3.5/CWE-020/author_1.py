import os
import yaml

def yaml_load(filename):
    if filename.endswith('.yaml') or filename.endswith('.yml'):
        with open(filename, 'r') as file:
            data = yaml.safe_load(file)
        return data
    else:
        raise ValueError('Invalid file type. Please provide a YAML file.')
