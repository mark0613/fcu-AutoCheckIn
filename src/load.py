import json

def load_json(json_path: str):
    content = ''
    with open(json_path) as file:
        content = json.load(file)
    return content