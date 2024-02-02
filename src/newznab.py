import requests
from xml.dom.minidom import parse, parseString


class Newznab:
    def __init__(self):
        self.url = None
        self.api_key = None
        self.response = None
        self.id = None
        self.query = None
        self.output_format = None
        self.doc = None
        self.categories = []
        self.items = []

    def caps(self):
        # Returns a list of caps that this newznab instance supports
        caps = "?t=caps"

        payload = {}
        headers = {
        }

        self.response = requests.request("GET", self.url + caps, headers=headers, data=payload)
        self.doc = parseString(self.response.text)

    def search(self):
        # The SEARCH function searches the index for items matching the search criteria. On successful search the
        # response contains a list of found items.
        search = "?t=search&q=" + self.query + "&apikey=" + self.api_key

        payload = {}
        headers = {
        }

        self.response = requests.request("GET", self.url + search, headers=headers, data=payload)
        self.doc = parseString(self.response.text)

    def details(self):
        # The response contains the generic RSS part + full extra information + full type/category specific information.
        details = "?t=details&id=" + self.id

        payload = {}
        headers = {
        }

        self.response = requests.request("GET", self.url + details + "&apikey=" + self.api_key, headers=headers,
                                         data=payload)
        self.doc = parseString(self.response.text)

    def get_nfo(self):
        # The GETNFO function returns a nfo file for a particular Usenet (NZB) item.
        nfo = "?t=info&id=" + self.id

        payload = {}
        headers = {
        }

        self.response = requests.request("GET", self.url + nfo, headers=headers, data=payload)
        self.doc = parseString(self.response.text)

    def get(self):
        # The GET function returns a nzb for a guid.
        get = "?t=get&id=" + self.id

        payload = {}
        headers = {
        }

        self.response = requests.request("GET", self.url + get, headers=headers, data=payload)
        self.doc = parseString(self.response.text)

    def parse_caps(self):
        # Parses the caps
        categories = self.doc.getElementsByTagName("category")
        for category in categories:
            self.categories.append({
                "id": category.getAttribute("id"),
                "name": category.getAttribute("name")
            })
        pass

    def parse_nfo(self):
        # Parses the nfo
        pass

    def parse_get(self):
        # Parses the get
        pass

    def parse_details(self):
        # Parses the details
        pass

    def parse_search(self):
        # Parses the search
        items = self.doc.getElementsByTagName("item")
        for item in items:
            item_data = {}
            for child in item.childNodes:
                if child.nodeType == child.ELEMENT_NODE:
                    if child.firstChild is not None:
                        item_data[child.tagName] = child.firstChild.nodeValue
                    else:
                        item_data[child.tagName] = None
            self.items.append(item_data)

    def test_conn(self):
        # Tests the connection to the newznab instance
        pass
