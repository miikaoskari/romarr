import json
import http.client
import os.path
import requests


class Igdb:
    def __init__(self, name=""):
        self.client_id = None
        self.secret_id = None
        self.access_id = None

    def get_config(self):
        script_dir = os.path.dirname(__file__)
        config_path = os.path.join(script_dir, "../config.json")
        config_path = os.path.normpath(config_path)
        config_json = open(config_path, "r")
        config = json.load(config_json)
        config_json.close()

        self.client_id = config["client_id"]
        self.access_id = config["access_id"]
        self.secret_id = config["secret_id"]

    def get_games_by_name(self, name):
        url = "https://api.igdb.com/v4/games"

        payload = f"fields cover, name, checksum, release_dates, dlcs, expansions, rating, screenshots, summary, url, artworks; search \"{name}\"; limit 5;"
        headers = {
            "Client-ID": f"{self.client_id}",
            "Authorization": f"Bearer {self.access_id}",
            "Accept": "application/json"
        }

        response = requests.post(url, data=payload, headers=headers)

        try:
            return response.json()
        except (KeyError, AttributeError) as e:
            print(f"Failed to parse games: {e}")
            return

    def get_game_by_id(self, game_id):
        url = "https://api.igdb.com/v4/games"

        payload = f"fields artworks, cover, dlcs, expansions, franchises, genres, name, platforms, rating, release_dates, screenshots, summary, url, checksum; where id = {game_id};"
        headers = {
            "Client-ID": f"{self.client_id}",
            "Authorization": f"Bearer {self.access_id}",
            "Accept": "application/json"
        }

        response = requests.post(url, data=payload, headers=headers)

        try:
            return response.json()
        except (KeyError, AttributeError) as e:
            print(f"Failed to parse game data: {e}")
            return

    def get_game_cover(self, cover_id):
        url = "https://api.igdb.com/v4/covers"

        payload = f"fields url; where id = {cover_id};"
        headers = {
            "Client-ID": f"{self.client_id}",
            "Authorization": f"Bearer {self.access_id}",
            "Accept": "application/json"
        }

        response = requests.post(url, data=payload, headers=headers)

        data = response.json()
        for item in data:
            item['url'] = item['url'].replace('t_thumb', 't_cover_big')

        try:
            return json.dumps(data, indent=2)
        except (KeyError, AttributeError) as e:
            print(f"Failed to parse cover data: {e}")
            return

    def get_game_screenshots(self, screenshot_id):
        url = "https://api.igdb.com/v4/screenshots"

        payload = f"fields url; where id = {screenshot_id};"
        headers = {
            "Client-ID": f"{self.client_id}",
            "Authorization": f"Bearer {self.access_id}",
            "Accept": "application/json"
        }

        response = requests.post(url, data=payload, headers=headers)
        
        data = response.json()
        for item in data:
            item['url'] = item['url'].replace('t_thumb', 't_cover_big')

        try:
            return json.dumps(data, indent=2)
        except (KeyError, AttributeError) as e:
            print(f"Failed to parse screenshot data: {e}")
            return

if __name__ == "__main__":
    igdb_query = Igdb("halo")
    igdb_query.get_config()
    print(igdb_query.get_game_cover(191111))

