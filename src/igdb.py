import json
import http.client


class Game:
    def __init__(self, name=""):
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

    def show_results(self):
        # print all the attributes of all the objects
        for attribute, value in self.__dict__.items():
            print(attribute, ":", value)

    def parse_results(self, data):
        data_dict = json.loads(data)
        for key in data_dict:
            if hasattr(self, key):
                setattr(self, key, data_dict[key])


class Igdb:
    def __init__(self, name=""):
        self.client_id = None
        self.secret_id = None
        self.access_id = None
        self.name = name
        self.games = []

    def get_config(self):
        config_json = open("../config.json", "r")
        config = json.load(config_json)

        self.client_id = config["client_id"]
        self.secret_id = config["secret_id"]
        self.access_id = config["access_id"]

        config_json.close()

    def search_game(self):
        conn = http.client.HTTPSConnection("api.igdb.com")
        payload = "fields *; search \"" + self.name + "\"; limit 1;"
        headers = {
            'Client-ID': self.client_id,
            'Authorization': 'Bearer ' + self.access_id,
            'Content-Type': 'application/json',
        }
        conn.request("POST", "/v4/games/", payload, headers)
        res = conn.getresponse()
        data = res.read()
        data_dict = json.loads(data.decode("utf-8"))
        for game in data_dict:
            game_obj = Game()
            game_obj.parse_results(json.dumps(game))
            self.games.append(game_obj)


search = Igdb("Halo")
search.get_config()
search.search_game()
search.games[0].show_results()
