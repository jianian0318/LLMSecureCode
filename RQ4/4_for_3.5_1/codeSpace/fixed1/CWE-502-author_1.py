import json

class Payload:
    def __init__(self, command):
        self.command = command
    
    def to_dict(self):
        return {
            "command": self.command
        }


def make_json_data(payload: Payload) -> str:
    return json.dumps(payload.to_dict())