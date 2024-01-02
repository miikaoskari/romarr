import xmlrpc.client


class Rtorrent:
    def __init__(self):
        self.url = None
        self.port = None
        self.username = None
        self.password = None
        self.server = None
        self.torrent = None

    def connect(self):
        self.server = xmlrpc.client.Server(self.url)


    def add_torrent(self):
        pass

    def get_torrents(self):
        mainview = self.server.download_list("", "main")
        torrent_list = []

        for torrent in mainview:
            torrent_list.append(self.server.d.name(torrent))
