import json

import yaml


def read_file(file_path):
    with open(file_path) as f:
        if file_path.endswith('.json'):
            return json.load(f)
        elif file_path.endswith(('.yml', '.yaml')):
            return yaml.safe_load(f)
        elif file_path.endswith('.txt'):
            return f.read()