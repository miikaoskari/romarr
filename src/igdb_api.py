import json

from igdb.wrapper import IGDBWrapper

class IGDBApi():
    def __init__(self, token: dict) -> None:
        self.token = token
        self.wrapper = IGDBWrapper(self.token['client_id'], self.token['access_token'])

    def _decode(self, byte_array: bytes) -> dict:
        text = byte_array.decode("utf-8")
        return json.loads(text)
    
    def _api_request(self, query: str):
        byte_array = self.wrapper.api_request("games", query)
        return self._decode(byte_array)

    def search_games(self, search: str, limit: int):
        query = f'search "{search}"; fields id,name,summary,cover.url,first_release_date; limit {limit};'
        return self._api_request(query)
