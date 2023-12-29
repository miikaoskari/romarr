import http.client


class Newznab:
    def __init__(self):
        self.url = None
        self.api_key = None
        self.response = None

    def caps(self):
        # Returns a list of caps that this newznab instance supports

        pass

    def register(self):
        # Registers this newznab instance with the master server
        pass

    def search(self):
        # The SEARCH function searches the index for items matching the search criteria. On successful search the
        # response contains a list of found items.
        pass

    def game_search(self):
        # Searches this newznab instance for the given query
        pass

    def details(self):
        # The response contains the generic RSS part + full extra information + full type/category specific information.
        pass

    def getnfo(self):
        # The GETNFO function returns an nfo file for a particular Usenet (NZB) item.
        pass

    def get(self):
        # The GET function returns an nzb for a guid.
        pass

    def comments(self):
        # The COMMENTS function returns comments for a particular Usenet (NZB) item.
        pass
