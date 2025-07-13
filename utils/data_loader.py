import json
import os


def load_login_data():
    file_path = os.path.join(os.path.dirname(__file__), '..', 'tests', 'login_data.json')
    with open(file_path, 'r') as file:
        return json.load(file)
