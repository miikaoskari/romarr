import xmlrpc.client


class Deluge:
    def __init__(self):
        self.server = None
        self.url = None
        self.username = None
        self.password = None
        self.client = None
        self.torrent = None
        self.port = None

    def connect(self):
        self.server = xmlrpc.client.Server(self.url + ":" + self.port)
        self.client = self.server.auth.login(self.username, self.password)

    def add_torrent(self):
        pass

    def get_torrents(self):
        pass
