import requests


class Person:
    def __init__(self, raw):
        self.raw = raw

        for key, value in raw.items():
            setattr(self, key, value)


class API:
    _HOST = 'https://yalies.io'
    _API_ROOT = '/api/'

    def __init__(self, token: str):
        self.token = token

    def post(self, endpoint: str, body: dict = {}):
        """
        Make a POST request to the API.

        :param params: dictionary of custom params to add to request.
        """
        headers = {
            'Authorization': 'Bearer ' + self.token,
        }
        request = requests.post(self._HOST + self._API_ROOT + endpoint,
                                json=body,
                                headers=headers)
        if request.ok:
            return request.json()
        else:
            raise Exception('API request failed. Received:\n' + request.text)

    def people(self, query=None, filters=None, page=None, page_size=None):
        """
        Given search criteria, get a list of matching people.
        """
        body = {
            'query': query,
            'filters': filters,
            'page': page,
            'page_size': page_size,
        }
        body = {k: v for k, v in body.items() if v}
        return [
            Person(person) for person in
            self.post('people', body=body)
        ]
