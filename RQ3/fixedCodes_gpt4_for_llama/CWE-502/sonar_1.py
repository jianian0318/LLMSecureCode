# Your code is correct, but to improve the security, you can include a type checking step before deserializing data. This way, you can ensure that only legitimate and expected types of objects are getting deserialized:

from flask import request
from yaml.constructor import SafeConstructor

class MySafeConstructor(SafeConstructor):
    def construct_python_str(self, node):
        return self.construct_yaml_str(node)

MySafeConstructor.add_constructor(
    "tag:yaml.org,2002:python/str",
    MySafeConstructor.construct_python_str)

yaml.SafeLoader.add_constructor('tag:yaml.org,2002:python/none', MySafeConstructor.none_constructor)
yaml.SafeLoader.add_constructor('tag:yaml.org,2002:python/bool', MySafeConstructor.bool_constructor)
yaml.SafeLoader.add_constructor('tag:yaml.org,2002:python/int', MySafeConstructor.int_constructor)
yaml.SafeLoader.add_constructor('tag:yaml.org,2002:python/float', MySafeConstructor.float_constructor)
yaml.SafeLoader.add_constructor('tag:yaml.org,2002:python/complex', MySafeConstructor.complex_constructor)
yaml.SafeLoader.add_constructor('tag:yaml.org,2002:python/str', MySafeConstructor.str_constructor)
yaml.SafeLoader.add_constructor('tag:yaml.org,2002:python/unicode', MySafeConstructor.unicode_constructor)
yaml.SafeLoader.add_constructor('tag:yaml.org,2002:python/list', MySafeConstructor.list_constructor)
yaml.SafeLoader.add_constructor('tag:yaml.org,2002:python/dict', MySafeConstructor.dict_constructor)

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    if request.method == 'POST':
        yaml_data = request.get_data()
        try:
            data = yaml.load(yaml_data, Loader=yaml.SafeLoader)
            return data
        except yaml.YAMLError as exc:
            return "Error: Invalid YAML data", 400
# Please take a look at the accepted YAML tags to make sure that no unwanted tags/types are serialized.