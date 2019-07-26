import json

def load_json_data(filename):
    ex_data = {}
    with open('exchanges.json') as json_file:
        ex_data = json.load(json_file)
    return ex_data