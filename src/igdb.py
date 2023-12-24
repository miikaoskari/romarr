import json
import http.client


class Metadata:
    def __init__(self, name=""):
        self.client_id = None
        self.secret_id = None
        self.access_id = None
        self.id = None
        self.alternative_names = None
        self.artworks = None
        self.category = None
        self.cover = None
        self.created_at = None
        self.final_release_date = None
        self.franchises = None
        self.game_modes = None
        self.involves_companies = None
        self.name = name
        self.parent_game = None
        self.platforms = None
        self.player_perspectives = None
        self.release_dates = None
        self.screenshots = None
        self.similar_games = None
        self.slug = None
        self.summary = None
        self.tags = None
        self.themes = None
        self.updated_at = None
        self.url = None
        self.websites = None
        self.checksum = None
        self.collections = None

    def get_config(self):
        config_json = open("../config.json", "r")
        config = json.load(config_json)

        self.client_id = config["client_id"]
        self.secret_id = config["secret_id"]
        self.access_id = config["access_id"]

        config_json.close()

    def search_game(self):
        conn = http.client.HTTPSConnection("api.igdb.com")
        payload = "fields *; search \"" + self.name + "\"; limit 10;"
        headers = {
            'Client-ID': self.client_id,
            'Authorization': 'Bearer ' + self.access_id,
            'Content-Type': 'application/json',
        }
        conn.request("POST", "/v4/games/", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

    def get_game_cover(self):
        conn = http.client.HTTPSConnection("api.igdb.com")
        payload = "fields *; where id=198580;"
        headers = {
            'Client-ID': self.client_id,
            'Authorization': 'Bearer ' + self.access_id,
            'Content-Type': 'application/json',
        }
        conn.request("POST", "/v4/covers", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

    def show_results(self):
        pass



