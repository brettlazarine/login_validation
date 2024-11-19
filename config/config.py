import json

def load_config():
    with open("appsettings.json", "r") as file:
        return json.load(file)

