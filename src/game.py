import json


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

    def get_small_description(self):
        return {
            "name": self.name,
            "summary": self.summary,
            "release_dates": self.release_dates,
            "cover_url": self.cover_url,
        }

    def show_results(self):
        # print all the attributes of all the objects
        for attribute, value in self.__dict__.items():
            print(attribute, ":", value)

    def parse_results(self, data):
        data_dict = json.loads(data)
        for key in data_dict:
            if hasattr(self, key):
                setattr(self, key, data_dict[key])
