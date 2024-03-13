import requests


class Sabnzbd:
    def __init__(self):
        self.api_key = None
        self.url = None

    def queue(self):

        pass

    def pause(self):
        pass

    def resume(self):
        pass

    def addfile(self):
        # Upload NZB using POST multipart/form-data. In your form, set the value of the field mode to addfile; the file
        # data should be in the field name or the field nzbfile.
        
        pass
