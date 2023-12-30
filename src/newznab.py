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

    def caps(self):
        # Returns a list of caps that this newznab instance supports
        caps = "?t=caps"

        payload = {}
        headers = {
        }

        self.response = requests.request("GET", self.url + caps, headers=headers, data=payload)

    def search(self):
        # The SEARCH function searches the index for items matching the search criteria. On successful search the
        # response contains a list of found items.
        search = "?t=search&q=" + self.query

        payload = {}
        headers = {
        }

        self.response = requests.request("GET", self.url + search, headers=headers, data=payload)

    def details(self):
        # The response contains the generic RSS part + full extra information + full type/category specific information.
        pass

    def get_nfo(self):
        # The GETNFO function returns a nfo file for a particular Usenet (NZB) item.
        nfo = "?t=info&id=" + self.id

        payload = {}
        headers = {
        }

        self.response = requests.request("GET", self.url + nfo, headers=headers, data=payload)

    def get(self):
        # The GET function returns a nzb for a guid.
        get = "?t=get&id=" + self.id

        payload = {}
        headers = {
        }

        self.response = requests.request("GET", self.url + get, headers=headers, data=payload)

    def parse_results(self):
        # Parses the results of the response
        list_of_errors = ['100', '101', '102', '103', '104', '105', '106', '107', '200', '201', '202', '203', '300',
                          '900', '910']

        if str(self.response.status_code) in list_of_errors:
            print("Error: " + self.response)
            return

        doc = parse(self.response)

        # Get the first child tag
        first_child_tag = doc.firstChild.tagName

        match first_child_tag:
            case "error":
                print("Error: " + self.response)
                return

            case "caps":
                self.parse_caps()

            case "nfo":
                self.parse_nfo()

            case "get":
                self.parse_get()

            case "details":
                self.parse_details()



    def parse_caps(self):
        # Parses the caps
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

    def test_conn(self):
        # Tests the connection to the newznab instance
        pass
