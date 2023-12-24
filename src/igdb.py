import json
import http.client


class Metadata:
    def __init__(self, client_id, secret_id, access_id):
        self.client_id = client_id
        self.secret_id = secret_id
        self.access_id = access_id


def get_config():
    config_json = open("../config.json", "r")
    config = json.load(config_json)

    client_id = config["client_id"]
    secret_id = config["secret_id"]
    access_id = config["access_id"]

    config_json.close()

    return client_id, secret_id, access_id


def search_game(name):
    client_id, secret_id, access_id = get_config()

    conn = http.client.HTTPSConnection("api.igdb.com")
    payload = "fields *; search \"" + name + "\"; limit 10;"
    headers = {
        'Client-ID': client_id,
        'Authorization': 'Bearer ' + access_id,
        'Content-Type': 'application/json',
    }
    conn.request("POST", "/v4/games/", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


def get_game_cover():
    client_id, secret_id, access_id = get_config()

    conn = http.client.HTTPSConnection("api.igdb.com")
    payload = "fields *; where id=198580;"
    headers = {
        'Client-ID': client_id,
        'Authorization': 'Bearer ' + access_id,
        'Content-Type': 'application/json',
    }
    conn.request("POST", "/v4/covers", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
