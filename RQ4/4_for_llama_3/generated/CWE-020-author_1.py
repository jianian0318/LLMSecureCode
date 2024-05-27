import yaml

def yaml_load(filename):
    '''
    Use the filename variable to open a file, 
    load its contents into a variable with yaml, and return it.
    '''
    try:
        with open(filename, 'r') as file:
            data = yaml.safe_load(file)
        return data
    except Exception as e:
        print(f"Error loading YAML file: {e}")
        return None

# Example usage
data = yaml_load('data.yaml')
print(data)