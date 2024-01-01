import qbittorrentapi


class Qbittorrent:
    def __init__(self):
        self.host = None
        self.port = None
        self.username = None
        self.password = None
        self.client = None
        self.torrent = None

    def connect(self):
        self.client = qbittorrentapi.Client(host=self.host, port=self.port, username=self.username,
                                            password=self.password)
        self.client.auth_log_in()

    def add_torrent(self):
        self.client.torrents_add(urls=self.torrent)

    def get_torrents(self):
        return self.client.torrents_info()
