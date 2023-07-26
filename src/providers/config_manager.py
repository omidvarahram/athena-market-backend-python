import json


def getConfigByKey(key_string):
    with open("src/data/config.json", 'r') as json_file:
        config = json.load(json_file)
        
        if config.get(key_string) is not None:
            return config[key_string]
        else:
            print (f"{key_string} not found")
