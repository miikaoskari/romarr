import json


# get client_id and secret_id from config.json
def get_config():
    config_json = open("../config.json", "r")
    config = json.load(config_json)

    client_id = config["client_id"]
    secret_id = config["secret_id"]

    config_json.close()

    return client_id, secret_id

def get_title():
    pass

def get_game():
    pass
