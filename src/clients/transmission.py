import requests

from transmission_rpc import Client


class Transmission:
    def __init__(self):
        self.url = None
        self.username = None
        self.password = None
        self.client = None
        self.torrent = None
        self.port = None

    def connect(self):
        self.client = Client(host=self.url, port=self.port, username=self.username, password=self.password)

    def add_torrent(self, torrent):
        self.torrent = torrent
        self.client.add_torrent(self.torrent)

    def get_torrents(self):
        return self.client.get_torrents()
