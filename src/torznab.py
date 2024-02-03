import requests
from xml.dom.minidom import parse, parseString


class Torznab:
    def __init__(self):
        self.url = None
        self.api_key = None
        self.response = None
        self.id = None
        self.query = None
        self.doc = None
        self.categories = []
        self.items = []
        self.torrent = None
        self.nfo = None
        self.details = []

    def caps(self):
        # Returns a list of caps that this torznab instance supports
        caps = "?t=caps" + "&apikey=" + self.api_key

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
        details = "?t=details&id=" + self.id + "&apikey=" + self.api_key

        payload = {}
        headers = {
        }

        self.response = requests.request("GET", self.url + details, headers=headers,
                                         data=payload)
        self.doc = parseString(self.response.text)

    def get_nfo(self):
        # The GETNFO function returns a nfo file for a particular Usenet (NZB) item.
        nfo = "?t=info&id=" + self.id + "&apikey=" + self.api_key

        payload = {}
        headers = {
        }

        self.response = requests.request("GET", self.url + nfo, headers=headers, data=payload)
        self.nfo = self.response.text

    def get(self):
        # The GET function returns a torrent for a guid.
        get = "?t=get&id=" + self.id + "&apikey=" + self.api_key

        payload = {}
        headers = {
        }

        self.response = requests.request("GET", self.url + get, headers=headers, data=payload)
        self.torrent = parseString(self.response.text)

    def parse_nfo(self):
        # Parses the nfo
        if self.nfo is not None:
            return self.nfo
        else:
            return None

    def parse_caps(self):
        # Parses the caps
        categories = self.doc.getElementsByTagName("category")
        for category in categories:
            self.categories.append({
                "id": category.getAttribute("id"),
                "name": category.getAttribute("name")
            })
            subcategories_elements = category.getElementsByTagName("subcat")
            for subcategory in subcategories_elements:
                self.categories.append({
                    "id": subcategory.getAttribute("id"),
                    "name": subcategory.getAttribute("name")
                })

    def parse_details(self):
        # Parses the details
        items = self.doc.getElementsByTagName("item")
        if items:
            item = items[0]
            item_data = {}
            for child in item.childNodes:
                if child.nodeType == child.ELEMENT_NODE:
                    if child.firstChild is not None:
                        item_data[child.tagName] = child.firstChild.nodeValue
                    else:
                        item_data[child.tagName] = None
            self.details.append(item_data)

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

