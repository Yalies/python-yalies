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
        self.headers = {
            'Authorization': 'Bearer ' + self.token,
        }

    def _get(self, endpoint: str):
        """
        Make a GET request to the API.
        """
        request = requests.get(self._HOST + self._API_ROOT + endpoint,
                                headers=self.headers)
        if request.ok:
            return request.json()
        else:
            raise Exception('API request failed. Received:\n' + request.text)

    def _post(self, endpoint: str, body: dict = {}):
        """
        Make a POST request to the API.
        """
        request = requests.post(self._HOST + self._API_ROOT + endpoint,
                                json=body,
                                headers=self.headers)
        if request.ok:
            return request.json()
        else:
            raise Exception('API request failed. Received:\n' + request.text)

    def filters(self):
        """
        Get a list of valid filters and recognized values.
        """
        return self._get('filters')

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
            self._post('people', body=body)
        ]

    def person(self, *args, **kwargs):
        """
        Given search criteria, return the first person found matching the desired parameters.
        """
        people = self.people(*args, **kwargs)
        if people:
            return people[0]
        return None
