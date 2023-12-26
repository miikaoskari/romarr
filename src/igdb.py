import json
import http.client


class Game:
    def __init__(self, name=""):
        self.id = None
        self.alternative_names = None
        self.artworks = None
        self.category = None
        self.cover = None
        self.cover_url = None
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

    @staticmethod
    def get_config():
        config_json = open("../config.json", "r")
        config = json.load(config_json)
        config_json.close()

        return config["client_id"], config["secret_id"], config["access_id"]

    def search_game(self):
        conn = http.client.HTTPSConnection("api.igdb.com")
        payload = f"fields *; search \"{self.name}\"; limit 10;"
        headers = {
            'Client-ID': self.client_id,
            'Authorization': 'Bearer ' + self.access_id,
            'Content-Type': 'application/json',
        }
        conn.request("POST", "/v4/games/", payload, headers)
        res = conn.getresponse()
        data = res.read()
        data_dict = json.loads(data.decode("utf-8"))
        for data in data_dict:
            game_obj = Game()
            game_obj.parse_results(json.dumps(data))
            self.games.append(game_obj)
            self.get_game_cover(game_obj)

    def get_game_cover(self, game_obj):
        conn = http.client.HTTPSConnection("api.igdb.com")
        payload = f"fields *; where id={game_obj.cover};"
        headers = {
            'Client-ID': self.client_id,
            'Authorization': 'Bearer ' + self.access_id,
            'Content-Type': 'application/json',
        }
        conn.request("POST", "/v4/covers", payload, headers)
        res = conn.getresponse()
        data = res.read()
        data_dict = json.loads(data.decode("utf-8"))
        if data_dict:
            url = data_dict[0]["url"]
            url = url.lstrip("//")
            game_obj.cover_url = url


client_id, secret_id, access_id = Igdb.get_config()
search1 = Igdb("Halo")
search1.client_id = client_id
search1.secret_id = secret_id
search1.access_id = access_id
search1.get_config()
search1.search_game()
for game in search1.games:
    game.show_results()
